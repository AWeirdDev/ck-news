import asyncio
from typing import Optional

import rjsonc
from primp import AsyncClient
from selectolax.lexbor import LexborHTMLParser, LexborNode

from .models import Classified, Message, MessageContent, File

BASE = "https://www.ck.tp.edu.tw"


def caturl(a: str, b: str) -> str:
    return a.rstrip("/") + "/" + b.lstrip("/")


def find_siteserver(parser: LexborHTMLParser) -> Optional[str]:
    """Find the site server Javascript file."""
    for script in parser.css("script"):
        src = script.attributes.get("src")
        if src and src.endswith("/siteserver"):
            return caturl(BASE, src)

    return None


def queried(
    class_id: str, /, *, n: int = 10, page: int = 1, text: Optional[str] = None
) -> dict:
    """Create a query that finds the latest `n` messages for a class.

    Args:
        class_id (str): The class ID.
        n (int, optional): Number of messages. Defaults to 10.
    """
    q = [
        {
            "between": {"max": "dtime", "min": "stime", "value": "now"},
            "match": {
                "classId": class_id,
                "hide": {
                    "$ne": class_id,
                },
                "released": True,
                "show": True,
                "status": "passed",
            },
        }
    ]
    if text:
        q.append(
            {
                "or": [
                    {"keyword": text},
                    {"text": {"name": text}},
                ],
            }
        )

    return {
        "option": {
            "between": {"max": "dtime", "min": "stime", "value": "now"},
            "match": {},
            "number": n,
            "page": page,
            "query": q,
            "sort": {"top": -1, "stime": -1, "mtime": -1, "ctime": -1, "dtime": -1},
        },
        "vector": "private",
        "static": False,
    }


def _htmd(ele: LexborNode) -> str:
    texts = []
    for element in ele.iter(include_text=True):
        if element.tag == "-text":
            texts.append(element.text())

        elif element.tag == "a":
            href = element.attributes.get("href", "") or ""  # to satisfy type checker

            if not href.startswith("http"):
                href = caturl(BASE, href)

            texts.append("[" + _htmd(element) + "](" + href + ")")

        elif element.tag == "b" or element.tag == "strong":
            texts.append("**" + _htmd(element) + "**")

        elif element.tag == "img":
            src = element.attributes.get("src", "") or ""

            if not src.startswith("http"):
                src = caturl(BASE, src)

            alt = element.attributes.get("alt", "") or ""

            texts.append("![" + alt + "](" + src + ")")

        elif element.tag == "br":
            texts.append("\n")

        elif element.tag == "ul":
            for inner_ele in element.iter(include_text=True):
                texts.append("- " + _htmd(inner_ele) + "\n")

        elif element.tag == "ol":
            for idx, inner_ele in enumerate(element.iter(include_text=True)):
                texts.append(f"{idx + 1}. " + _htmd(inner_ele) + "\n")

        else:
            texts.append(_htmd(element))

    return " ".join(texts).strip()


def html_to_md(html: str) -> str:
    parser = LexborHTMLParser(html)
    if not parser.body:
        return ""
    return _htmd(parser.body)


class CkClient:
    """A client for fetching latest messages & news on [cktp](https://www.ck.tp.edu.tw/).

    # DISCLAIMER
    EDUCATIONAL PURPOSES ONLY.
    THIS IS SOLELY A DEMONSTRATION ON HOW DATA FETCHING IS POSSIBLE VIA MODERN TOOLING.
    USE AT YOUR OWN RISK.

    # Example
    ```python
    client = CkClient()
    news = await client.get_news()
    print(len(news))
    ```
    """

    client: AsyncClient

    def __init__(self):
        self.client = AsyncClient(
            impersonate="chrome_133", cookie_store=True, referer=True
        )

    async def get_news(
        self, *, n: int = 10, page: int = 1, text: Optional[str] = None
    ) -> list[Classified]:
        """Get the news.

        Don't use this too often. Use at your own risk.

        Args:
            n (int, optional): Number of messages.
            page (int, optional): Page.
            text (str, optional): Text query.
        """
        res = await self.client.get("https://www.ck.tp.edu.tw/nss/p/index")
        parser = LexborHTMLParser(res.content)

        siteserver = find_siteserver(parser)
        if not siteserver:
            raise RuntimeError("could not find siteserver")

        ss_res = await self.client.get(siteserver)

        dmap_str = ""
        for line in ss_res.text.splitlines():
            if dmap_str:
                if line.strip() == "];":
                    dmap_str += "]"
                    break

                dmap_str += line

            elif line.startswith("const deployMap"):
                dmap_str = "["
        else:
            raise RuntimeError("could not find deployMap in siteserver")

        # rjsonc is my pookie
        # it's more tolerant uwu
        deployments = rjsonc.loads(dmap_str)

        results = []

        for deployment in deployments:
            # yes, it took some js digging
            # to find out what these actually mean
            # like... wtf just gimme the full thing
            module_id = deployment["mid"]
            section_id = deployment["sid"]  # ok this is just my guess

            classes = await self.fetch_class_ids(module_id, section_id)
            if not classes:
                continue

            for name, ident in classes:
                results.append(
                    asyncio.create_task(
                        self.get_classified_news(
                            module_id,
                            section_id,
                            name,
                            ident,
                            n=n,
                            page=page,
                            text=text,
                        )
                    )
                )

        return await asyncio.gather(*results)

    async def fetch_class_ids(
        self, mid: str, sid: str
    ) -> Optional[list[tuple[str, str]]]:
        res = await self.client.get(
            f"https://www.ck.tp.edu.tw/nss/site/main/storage/{mid}/{sid}/single",
            params={"vector": "private", "static": "false"},
        )
        json = res.json()
        if json["error"]:
            # non-zero, but i dont care lmfao
            return

        if not json["data"] or "data" not in json["data"]:
            return

        data = json["data"]["data"]
        if "class" not in data:
            return

        return [(cl["name"], cl["id"]) for cl in data["class"]]

    async def get_classified_news(
        self,
        module_id: str,
        section_id: str,
        class_name: str,
        class_ident: str,
        /,
        *,
        n: int = 10,
        page: int = 1,
        text: Optional[str] = None,
    ) -> Classified:
        res = await self.client.post(
            f"https://www.ck.tp.edu.tw/nss/site/main/storage/{module_id}/{section_id}/find",
            json=queried(class_ident, n=n, page=page, text=text),
        )
        messages = []
        items = res.json()["data"]["result"]

        for item in items:
            message_id = item["_id"]
            visits = item["visit"]
            ctime = item["ctime"]
            utime = item["utime"]
            keywords = item["keyword"]
            if keywords and isinstance(keywords[-1], list):
                keywords.pop()  # literally have no idea what that is

            data = item["data"]
            announcer_name = data["annoName"]
            title = data["name"]
            content_html = data["content"]
            files = data.get("ext", [])

            messages.append(
                Message(
                    id=message_id,
                    visits=visits,
                    ctime=ctime,
                    utime=utime,
                    keywords=keywords,
                    announcer=announcer_name,
                    title=title,
                    content=MessageContent(
                        html=content_html,
                        markdown=html_to_md(content_html),
                    ),
                    files=[
                        File(
                            name=file["name"],
                            url=caturl(BASE, file["url"]),
                        )
                        for file in files
                    ],
                )
            )

        return Classified(
            id=class_ident,
            name=class_name,
            module_id=module_id,
            section_id=section_id,
            rss=f"https://www.ck.tp.edu.tw/nss/main/feeder/{module_id}/{section_id}?f=normal&%240={class_ident}&vector=private&static=false",
            messages=messages,
        )

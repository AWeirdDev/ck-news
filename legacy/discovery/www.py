import rjsonc
from primp import Client
from selectolax.lexbor import LexborHTMLParser

client = Client(impersonate="chrome_133", cookie_store=True, referer=True)
res = client.get("https://www.ck.tp.edu.tw/nss/p/index")

parser = LexborHTMLParser(res.content)

for script in parser.css("script"):
    src = script.attributes.get("src")
    if src and src.endswith("/siteserver"):
        break
else:
    raise RuntimeError("could not find siteserver, oop")

res = client.get("https://www.ck.tp.edu.tw" + src)
js = res.text

d = ""
for line in js.splitlines():
    if d:
        if line == "];":
            d += "]"
            break

        d += line

    if line.startswith("const deployMap"):
        d = "["
else:
    raise RuntimeError("failed to collect deployMap")

deployed_items = rjsonc.loads(d)


def queried(class_id: str) -> dict:
    return {
        "option": {
            "between": {"max": "dtime", "min": "stime", "value": "now"},
            "match": {},
            "number": 10,
            "page": 1,
            "query": [
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
            ],
            "sort": {"top": -1, "stime": -1, "mtime": -1, "ctime": -1, "dtime": -1},
        },
        "vector": "private",
        "static": False,
    }


# we're gonna get the "single" item idk what that means lol
"https://www.ck.tp.edu.tw/nss/site/main/storage/5abf2d62aa93092cee58ceb4/KG5mY0d9355/single?vector=private&static=false"


def get_class_ids(mid: str, sid: str):
    res = client.get(
        f"https://www.ck.tp.edu.tw/nss/site/main/storage/{mid}/{sid}/single",
        params={"vector": "private", "static": "false"},
    )
    json = res.json()
    if json["error"]:
        print("error", json["msg"])
        return

    if (
        not json["data"]
        or "data" not in json["data"]
        or "class" not in json["data"]["data"]
    ):
        return

    data = json["data"]["data"]

    return {cl["name"]: cl["id"] for cl in data["class"]}


for item in deployed_items:
    mid = item["mid"]
    sid = item["sid"]

    class_ids = get_class_ids(mid, sid)
    if class_ids is None:
        continue

    for class_id in class_ids.values():
        print("!!!!!!!!!!!!!! class id:", class_id)
        res = client.post(
            "https://www.ck.tp.edu.tw/nss/site/main/storage/"
            + mid
            + "/"
            + sid
            + "/find",
            json=queried(class_id),
        )

        items = res.json()["data"]["result"]

        for item in items:
            visits = item["visit"]
            ctime = item["ctime"]  # i think this is the time it gets posted?
            utime = item[
                "utime"
            ]  # i think this is the time it gets uh.. removed????? bcuz like... 'u' probably goes with "un-xxx"
            data = item["data"]
            keywords = item["keyword"]

            content = data["content"]
            p = LexborHTMLParser(content)
            print(data["name"], "-", ctime, utime)

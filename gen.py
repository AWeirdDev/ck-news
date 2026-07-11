# pyright: reportMissingTypeStubs=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
# pyright: reportUnknownVariableType=false, reportUnusedCallResult=false

import os

import feedparser
from primp import Client

from vendor.htmlstr import MarkdownTransformer, Parser

IMPORTANT_NOTICE_URL = (
    "https://www.ck.tp.edu.tw/nss/main/feeder/5abf2d62aa93092cee58ceb4"
    "/KG5mY0d9355?f=normal&%240=hhyrNQJ0110&vector=private&static=false"
)
LATEST_NEWS_URL = (
    "https://www.ck.tp.edu.tw/nss/main/feeder/5abf2d62aa93092cee58ceb4"
    "/IXZld9j7619?f=normal&%240=kpenVCJ9015&vector=private&static=false"
)

client = Client()
res = client.get(IMPORTANT_NOTICE_URL)

feed = feedparser.parse(res.text)


texts = []

for item in feed.entries:
    print("Added:", item.get("title"))

    parser = Parser()
    elements = parser.parse(str(item.get("description")))

    text = f"## [{item.get('title')}]({item.get('link')})"

    transformer = MarkdownTransformer(elements)
    text += transformer.text()
    texts.append(text)

os.makedirs("dist", exist_ok=True)

with open("dist/index.md", "w") as f:
    f.write('<base href="https://www.ck.tp.edu.tw/" />\n\n' + "\n\n***\n\n".join(texts))

print()
print("=====> built.")

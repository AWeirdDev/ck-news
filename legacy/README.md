At the time of writing (2025-11-26), this does not work anymore, but I'll put it here for future reference.
This proves that scraping prevention is pretty bad on this site.

Anyhow, if you'd like, you can [contact me](https://github.com/AWeirdDev) if you want to talk about this.

***

# ck-api

堅果中學公告擷取 API。

這個 Repo 可以大致分成三個部分：

- `main.py` – REST API。使用 `uvicorn` 和 `fastapi`。
- `discovery/*` – 資料探索。
- `ckapi/*` – 可使用的模組。

你可以下載這個 Repo，並自己試試：

```sh
git clone https://github.com/AWeirdDev/ck-api
```

```python
from ckapi import CkClient

client = CkClient()
news = await client.get_news()

print(news)
```

<details>
<summary><b>Output (obscured)</b></summary>

```python
[
    Classified(
        id='kpenVCJ9015', 
        name='全部消息', 
        module_id='5abf2d62aa93092cee58ceb4', 
        section_id='IXZld9j7619', 

        # rss feed
        rss='https://www.ck.tp.edu.tw/nss/main/feeder/5abf2d62aa93092cee58ceb4/IXZld9j7619?f=normal&%240=kpenVCJ9015&vector=private&static=false', 
        
        messages=[
            Message(
                id='68b1658afe9e9455cc0e4993', 
                visits=28, 
                ctime='2025-08-29T08:32:10.402Z', 
                utime='2025-08-30T08:01:45.023Z', 
                keywords=[
                    # obscured
                    '???', 
                    '???', 
                    '??組'
                ], 
                announcer='??組', 
                title='???', 
                content=MessageContent(
                    html='<p><a href="https://www.example.com">辦法</a></p>', 
                    markdown='[辦法](https://www.example.com)'
                ),
                files=[
                    File(
                        name='example.pdf', 
                        url='https://www.ck.tp.edu.tw/uploads/example.pdf'
                    )
                ]
            ),
            ... # more messages
        ]
    ),
    ... # more items
]
```

</details>

## REST API
```http
GET http://localhost:8000/news
```

**Query parameters**:
- `n` – Optional. Number of items.
- `page` – Optional. Page #.
- `text` – Optional. Text filter.

## How?
There's this [CK app](https://apps.apple.com/app/id6608961910) made by our beloved senpai uwu (very cool)

...but bro just hasn't been updating it for over a year, and the "latest news" feature isn't working.
As a pedantic (kind of) developer myself I am NOT happy about this shi. So, I decided to make my own *fetcher* (Actually, I tried to make my own app first with Expo, but the project structure looked so hawwwd, so I'm not learning that for now).

1. We visit the [index page](https://www.ck.tp.edu.tw/nss/p/index) and iterate through the script elements to find `siteserver` (possibly the backend server). I won't be hardcoding the static URL as it might change for later versions of the site (judging by the ID, it doesn't look man-made at all).
2. We fetch the `siteserver`, and the server returns Javascript code. One line starts with `const deployMap = [`, which specifies some deployments, as far as I know.
3. We loop through the deployments to find **module IDs** and **section IDs**. Note that the term "section" is assumed, as the actual identifier is called `sid`. The same applies for `mid`.
4. We call the `/single` endpoint for individual module ID and section ID pairs, and some of them returns **class IDs** (for better message filtering).
5. With the module, section & class IDs, we can now query the messages!

It's actually possible to fetch messages without class IDs, but the output would be super messy and... unwanted! (Some are even test messages when they first published this site.)

## License
Licensed under MIT.

***

# DISCLAIMER

THE SOLE PURPOSE OF THIS REPOSITORY IS TO PROVE THE POSSIBILITY OF UTILIZING MODERN TOOLS FOR FETCHING DATA, AND IS FOR EDUCATIONAL PURPOSES ONLY.
AS STATED IN THE `robots.txt` FILE IN THE OFFICIAL SITE:

```yml
User-agent: *
Allow: /nss/
Allow: /public/
Allow: /uploads/
Allow: /sitemap/
Sitemap: https://www.ck.tp.edu.tw/sitemap.xml
```

...ANY USER AGENT IS ALLOWED, AND THE SITES THIS PROGRAM VISITS IS ALWAYS UNDER THE SCOPE OF `/nss/`.
AS OF THE VERSION OF `robots.txt` FOUND ON 2025-08-30, THE BEHAVIORS OF THIS PROGRAM DO NOT VIOLATE THE ROBOTS TEXT.
[VIEW ON WAYBACK MACHINE (INTERNET ARCHIVE)](https://web.archive.org/web/20250830100619/https://www.ck.tp.edu.tw/robots.txt).

**EDUCATIONAL PURPOSES ONLY. MISUSE AND ABUSE IS STRICTLY PROHIBITED.**

This project is not affiiliated with _Taipei Municipal Chien Kuo High School_.**

***

(c) 2025 AWeirdDev

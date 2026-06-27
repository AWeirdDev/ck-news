import asyncio
from ckapi import CkClient

client = CkClient()


async def main():
    news = await client.get_news()
    print(news[0])


asyncio.run(main())

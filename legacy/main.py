from typing import Optional
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from ckapi import CkClient, Classified

app = FastAPI()
client = CkClient()


def error(msg: str, /) -> JSONResponse:
    return JSONResponse(
        {"type": "error", "error": {"message": msg}},
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


@app.get("/")
async def index():
    return JSONResponse({})


@app.get("/news", response_model=list[Classified])
async def news(n: int = 10, page: int = 1, text: Optional[str] = None):
    try:
        return await client.get_news(n=n, page=page, text=text)
    except RuntimeError as err:
        return error(str(err))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)

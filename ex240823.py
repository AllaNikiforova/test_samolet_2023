from fastapi import FastAPI
from pydantic import BaseModel
import httpx
import uvicorn


class NewsItem(BaseModel):
    title: str
    description: str


app = FastAPI()


@app.get("/", response_model=NewsItem)
async def get_news():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://webapi.autodoc.ru/api/news/1/1")
        data = response.json()

    news = data.get("news", [])
    if len(news):
        title = news[0].get("title", "")
        description = news[0].get("description", "")
    else:
        title = ""
        description = ""

    news_item = NewsItem(title=title, description=description)
    return news_item
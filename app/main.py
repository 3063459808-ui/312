from fastapi import FastAPI

app = FastAPI(
    title="News Summarizer API",
    description="An API to fetch and summarize news articles.",
    version="1.0.0",
)

from .routers import news

app.include_router(news.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the News Summarizer API"}

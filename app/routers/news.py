from fastapi import APIRouter, Query, HTTPException
from typing import List, Dict, Any
from ..services.news_service import news_service_instance

router = APIRouter(
    prefix="/news",
    tags=["news"],
    responses={404: {"description": "Not found"}},
)

@router.get("/headlines",
            response_model=List[Dict[str, str]],
            summary="Get Latest News Headlines",
            description="Fetches a list of the latest news headlines from the configured RSS feed.")
def get_headlines_endpoint():
    """
    Provides a list of the latest news headlines.
    Each headline is a dictionary containing a title and a link.
    """
    return news_service_instance.get_headlines()

@router.get("/summarize",
            response_model=Dict[str, str],
            summary="Summarize an Article",
            description="Fetches and summarizes an article from a given URL.")
def get_summary_endpoint(url: str = Query(...,
                                  description="The full URL of the article to be summarized.",
                                  example="http://www.news.cn/world/2022-12/14/c_1129207152.htm")):
    """
    Takes a URL as a query parameter, fetches the article content,
    and returns a summary of the article.
    """
    if not url.startswith("http://") and not url.startswith("https://"):
        raise HTTPException(
            status_code=400,
            detail="Invalid URL. Please provide a full URL starting with http:// or https://"
        )

    return news_service_instance.get_summary(url)

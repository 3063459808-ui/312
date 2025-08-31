import feedparser
import requests
from bs4 import BeautifulSoup
import re
from fastapi import HTTPException

class NewsService:
    def __init__(self):
        self.rss_url = "http://www.xinhuanet.com/world/news_world.xml"

    def get_headlines(self) -> list[dict]:
        """
        Fetches and parses the RSS feed to get latest headlines.
        Returns a list of dictionaries, e.g., [{"title": "...", "link": "..."}]
        """
        try:
            feed = feedparser.parse(self.rss_url)
            if feed.bozo:
                raise HTTPException(status_code=500, detail=f"Failed to parse RSS feed: {feed.bozo_exception}")

            headlines = []
            for entry in feed.entries[:15]: # Get top 15
                headlines.append({"title": entry.title, "link": entry.link})
            return headlines
        except Exception as e:
            # This catches potential network errors from feedparser's side
            raise HTTPException(status_code=500, detail=f"Error fetching RSS feed: {e}")


    def get_summary(self, url: str) -> dict:
        """
        Fetches an article from a URL, extracts its text, and returns a summary.
        """
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'lxml')

            # This selector is specific to news.cn article structure.
            # It targets the div that contains the main article body.
            content_div = soup.find('div', id='detail')
            if not content_div:
                # Fallback to getting all paragraphs if the specific div is not found
                paragraphs = soup.find_all('p')
            else:
                paragraphs = content_div.find_all('p')

            full_text = ' '.join(p.get_text().strip() for p in paragraphs)

            if not full_text.strip():
                raise HTTPException(status_code=404, detail="Could not extract article text from the page.")

            summary = self._summarize_text(full_text)
            return {"url": url, "summary": summary}

        except requests.RequestException as e:
            raise HTTPException(status_code=502, detail=f"Failed to fetch the article URL: {e}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")

    def _summarize_text(self, text: str, sentence_count: int = 3) -> str:
        """
        A simple extractive summarizer for Chinese text.
        """
        if not text:
            return ""

        # Clean up whitespace and join lines
        text = text.replace('\n', '').replace('\r', '').replace(' ', '').strip()

        # Split sentences based on Chinese punctuation
        sentences = re.split(r'([。！？])', text)

        # Group sentences back with their punctuation
        grouped_sentences = []
        for i in range(0, len(sentences) - 1, 2):
            grouped_sentences.append(sentences[i] + sentences[i+1])

        # Handle case where the text doesn't end with punctuation
        if len(sentences) % 2 == 1 and sentences[-1]:
            grouped_sentences.append(sentences[-1])

        # Filter out short/empty fragments
        valid_sentences = [s for s in grouped_sentences if len(s) > 5]

        summary = "".join(valid_sentences[:sentence_count])
        return summary

# Singleton instance to be used by routers
news_service_instance = NewsService()

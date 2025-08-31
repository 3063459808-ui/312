import feedparser
import sys

# Using the Xinhua RSS feed URL that was successful
RSS_URL = "http://www.xinhuanet.com/world/news_world.xml"

def fetch_and_print_headlines():
    """
    Fetches and parses the RSS feed.
    Prints headlines and links in a machine-readable format: "Title|||Link".
    """
    try:
        # Note: This script relies on the execution environment having network access
        # and the 'feedparser' library installed.
        feed = feedparser.parse(RSS_URL)
        if feed.bozo:
            print(f"ERROR: Malformed feed: {feed.bozo_exception}", file=sys.stderr)
            return

        separator = "|||"
        for entry in feed.entries[:15]: # Get top 15 articles
            title = entry.title.replace('\n', ' ').strip()
            link = entry.link.strip()
            print(f"{title}{separator}{link}")

    except Exception as e:
        print(f"ERROR: An exception occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    fetch_and_print_headlines()

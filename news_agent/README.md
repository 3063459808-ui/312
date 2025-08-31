# News Summarizer Agent

This project contains a set of scripts to fetch and summarize news articles.

## Components

- `get_headlines.py`: This script fetches the latest 15 headlines from the Xinhua News RSS feed. It prints the titles and links to standard output, separated by `|||`. **Note:** This script requires the `feedparser` library and network access from its execution environment.

- `summarize.py`: This script reads text from standard input, and prints a 3-sentence summary of that text to standard output.

- `requirements.txt`: Contains the necessary Python packages (`feedparser`).

## Orchestrated Workflow

This agent is not designed to be run as a single interactive script. It is orchestrated by a controlling agent (like Jules) in the following way:

1.  The controlling agent fetches the raw text of the news RSS feed using its own tools (e.g., `view_text_website`).
2.  The agent parses this text to extract a list of article titles and URLs.
3.  The agent presents the list of titles to the user and asks them to choose one.
4.  The agent fetches the full text of the chosen article from its URL.
5.  The agent provides the fetched text as standard input to the `summarize.py` script (`python summarize.py`).
6.  The output of the summarizer is captured and displayed to the user.

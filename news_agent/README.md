# News Summarizer Agent

This project contains a set of scripts to fetch and summarize news articles.

## Components

- `get_headlines.py`: This script fetches the latest 15 headlines from the Reuters World News RSS feed. It prints the titles and links to standard output, separated by `|||`.

- `summarize.py`: This script reads text from standard input, and prints a 3-sentence summary of that text to standard output.

- `requirements.txt`: Contains the necessary Python packages (`feedparser`).

## Workflow

This agent is not run as a single interactive script. It is orchestrated by a controlling agent (like Jules) in the following way:

1.  Run `python get_headlines.py` to get a list of articles.
2.  The output is parsed to show the user a numbered list of headlines.
3.  The user chooses an article.
4.  The agent fetches the full text of the article from the chosen URL using its own tools.
5.  The fetched text is piped as standard input to `python summarize.py`.
6.  The output of the summarizer is captured and displayed to the user.

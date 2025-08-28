# Simple Question Answering Agent

This is a very simple command-line agent that answers questions based on a local knowledge base file (`knowledge.txt`).

## Functionality

- The agent reads facts from `knowledge.txt`.
- It takes a user's question from the command line.
- It finds sentences in `knowledge.txt` that contain keywords from the question.
- It returns the matching sentences as the answer.

## How to Run

1.  Navigate to the `simple_agent` directory.
    ```bash
    cd simple_agent
    ```
2.  Run the agent script using Python.
    ```bash
    python agent.py
    ```
3.  Ask questions related to the content in `knowledge.txt`.
4.  Type `exit` or `quit` to stop the agent.

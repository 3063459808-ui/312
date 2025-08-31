import sys
import re

def summarize_text(text, sentence_count=3):
    """
    A simple extractive summarizer.
    It takes a block of text and returns the first N sentences.
    """
    if not text or not text.strip():
        return ""

    # Replace newlines with spaces for better sentence parsing
    text = text.replace('\n', ' ').strip()

    # Use regex to split sentences more reliably than just '.'.
    # This looks for ., !, ? followed by a space or end of string.
    # It handles cases like "Dr. Smith" better than simpler splits.
    sentences = re.split(r'(?<=[.!?])\s+', text)

    # Take the first N sentences and filter out any empty ones.
    summary_sentences = [s.strip() for s in sentences if s.strip()][:sentence_count]

    summary = " ".join(summary_sentences)

    # Ensure the summary ends with punctuation if it had it.
    if summary and summary[-1] not in ".!?":
        # Find the last punctuation in the original text of the last sentence
        original_last_sentence = summary_sentences[-1]
        if original_last_sentence and original_last_sentence[-1] in ".!?":
             summary += original_last_sentence[-1]

    return summary

def main():
    """Reads text from stdin and prints a summary to stdout."""
    try:
        input_text = sys.stdin.read()
        summary = summarize_text(input_text)
        print(summary)
    except Exception as e:
        print(f"ERROR: Could not generate summary. {e}", file=sys.stderr)


if __name__ == "__main__":
    main()

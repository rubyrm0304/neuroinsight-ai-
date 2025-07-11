from transformers import pipeline

summarizer = pipeline("summarization", model="t5-small")

def summarize_text(text):
    max_chunk = 500
    chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]
    summaries = [summarizer(chunk, max_length=150, min_length=40)[0]["summary_text"] for chunk in chunks]
    return "\n\n".join(summaries)

from fastapi import FastAPI
from utils.preprocess import clean_text
from analyzer.sentiment import get_sentiment
from analyzer.topic import get_topic
from analyzer.summarizer import get_summary
from analyzer.bias import detect_bias

app = FastAPI()

@app.post("/analyze")
def analyze(text: str):
    cleaned = clean_text(text)

    sentiment, score = get_sentiment(cleaned)
    topic = get_topic(cleaned)
    summary = get_summary(cleaned)
    bias = detect_bias(cleaned)

    return {
        "summary": summary,
        "sentiment": sentiment,
        "confidence": score,
        "topic": topic,
        "bias": bias
    }
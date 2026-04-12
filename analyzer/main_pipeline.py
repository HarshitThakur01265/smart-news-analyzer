from analyzer.sentiment import get_sentiment
from analyzer.topic import classify_topic
from analyzer.summarizer import get_summary
from analyzer.bias import detect_bias
from analyzer.fake_news import detect_fake_news


def analyze_news(text):

    # 🔹 Step 1: Sentiment
    sentiment = get_sentiment(text)

    # 🔹 Step 2: Topic
    topic = classify_topic(text)

    # 🔹 Step 3: Summary
    summary = get_summary(text)

    # 🔹 Step 4: Bias
    bias = detect_bias(text)

    # 🔹 Step 5: Fake News Detection
    fake_news = detect_fake_news(text)

    # 🔹 Combine everything
    result = {
        "sentiment": sentiment,
        "topic": topic,
        "summary": summary,
        "bias": bias,
        "fake_news": fake_news
    }

    return result
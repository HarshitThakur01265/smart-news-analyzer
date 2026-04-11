from analyzer.sentiment import get_sentiment
from analyzer.bias import detect_bias

def detect_fake_news(text):
    sentiment = get_sentiment(text)
    bias = detect_bias(text)

    sentiment_label = sentiment
    bias_label = bias['label']
    bias_score = bias['score']

    # Simple logic
    if bias_label in ["biased", "manipulative"] and bias_score > 0.6:
        return {
            "prediction": "Fake News",
            "reason": "High bias and manipulative tone detected"
        }

    elif sentiment_label == "NEGATIVE" and bias_label != "neutral":
        return {
            "prediction": "Possibly Misleading",
            "reason": "Negative tone with bias"
        }

    else:
        return {
            "prediction": "Likely Real",
            "reason": "Neutral tone and low bias"
        }
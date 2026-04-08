from analyzer.sentiment import get_sentiment

text = "This government policy is terrible and harmful."

label, score = get_sentiment(text)

print("Sentiment:", label)
print("Confidence:", score)
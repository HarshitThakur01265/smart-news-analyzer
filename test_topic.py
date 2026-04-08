from analyzer.topic import get_topic

text = "The government passed a new law regarding elections."

topic, score = get_topic(text)

print("Topic:", topic)
print("Confidence:", score)
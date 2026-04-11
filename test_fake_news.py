from analyzer.fake_news import detect_fake_news

text = "The corrupt government is secretly destroying the nation with hidden agendas."

result = detect_fake_news(text)

print("Prediction:", result['prediction'])
print("Reason:", result['reason'])
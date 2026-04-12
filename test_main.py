from analyzer.main_pipeline import analyze_news

text = "The corrupt government is secretly destroying the nation with terrible policies."

result = analyze_news(text)

for key, value in result.items():
    print(f"\n{key.upper()}:\n", value)
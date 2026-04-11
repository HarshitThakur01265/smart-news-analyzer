from analyzer.bias import detect_bias

text = "The corrupt government is destroying the country with terrible policies."

result = detect_bias(text)

print("Bias Label:", result['label'])
print("Confidence:", result['score'])
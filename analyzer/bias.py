def detect_bias(text):
    bias_words = ["shocking", "truth", "secret", "exposed", "they dont want"]

    score = sum(word in text for word in bias_words)

    if score >= 2:
        return "High"
    elif score == 1:
        return "Medium"
    return "Low"
import re

def clean_text(text):
    text = text.lower()  # normalize
    text = re.sub(r"http\S+", "", text)  # remove URLs
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # remove special chars
    return text
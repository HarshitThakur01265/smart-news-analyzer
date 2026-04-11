from transformers import pipeline

# Load model ONCE (important optimization)
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def get_sentiment(text):
    result = sentiment_pipeline(text)[0]
    
    label = result['label']
    score = result['score']
    
    return label, score
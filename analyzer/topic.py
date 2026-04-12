from transformers import pipeline

# Load zero-shot classification model
topic_pipeline = pipeline("zero-shot-classification")

def classify_topic(text):
    candidate_labels = [
        "Politics",
        "Technology",
        "Business",
        "Health",
        "Sports",
        "Entertainment",
        "Education"
    ]
    
    result = topic_pipeline(text, candidate_labels)
    
    topic = result['labels'][0]
    score = result['scores'][0]
    
    return topic, score
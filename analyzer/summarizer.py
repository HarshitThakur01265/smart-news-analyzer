from transformers import pipeline

summarizer = pipeline("summarization")

def get_summary(text):
    result = summarizer(
        text,
        max_length=80,
        min_length=30,
        do_sample=False
    )
    
    return result[0]['summary_text']
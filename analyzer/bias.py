from transformers import pipeline

bias_classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

def detect_bias(text):
    labels = ["neutral", "biased", "manipulative"]

    result = bias_classifier(text, labels)

    return {
        "label": result['labels'][0],
        "score": result['scores'][0]
    }
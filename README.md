# Smart News Analyzer

A Flask-based web application that analyzes news articles for sentiment, topics, summary, and bias.

## Structure
```
smart-news-analyzer/
├── app.py              # Main Flask app
├── analyzer/           # Analysis modules
│   ├── sentiment.py
│   ├── topic.py
│   ├── summarizer.py
│   └── bias.py
├── utils/              # Utility functions
│   └── preprocess.py
├── requirements.txt    # Dependencies
└── README.md
```

## Setup
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Download NLTK data (run in Python):
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```
3. Run the app:
   ```
   python app.py
   ```

## API Usage
POST `/analyze` with JSON `{"text": "your news article"}`

Returns JSON with analysis results.

## TODO
- Implement real ML models in analyzer modules.
- Add frontend.
- Deploy to cloud.

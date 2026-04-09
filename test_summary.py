from analyzer.summarizer import get_summary

text = """
Artificial Intelligence is rapidly evolving and impacting various industries. 
It helps automate repetitive tasks, improve decision-making, and enhance efficiency. 
Companies are investing heavily in AI technologies to stay competitive.
"""

summary = get_summary(text)

print("Summary:", summary)
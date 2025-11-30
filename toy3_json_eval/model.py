from transformers import pipeline
import json
from pathlib import Path


sentiment_pipeline = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def predict_label(text: str) -> str: # input example: "I love programming!", output example: "POSITIVE"
    print(text)
    result = sentiment_pipeline(text) # outptut example: {'label': 'POSITIVE', 'score': 0.9998}
    print(result)

data_path = Path(__file__).parent / "data.json"

with open(data_path, "r") as f:
    data = json.load(f)

for item in data:
    text = item['text']
    predict_label(text)    

  
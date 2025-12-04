from transformers import pipeline



sentiment_pipeline = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def predict_label(text: str) -> str: # input example: "I love programming!", output example: "POSITIVE"
    #print(text)
    result = sentiment_pipeline(text)[0] # outptut example: {'label': 'POSITIVE', 'score': 0.9998}
    #print(result)
    return result['label'].lower()



  
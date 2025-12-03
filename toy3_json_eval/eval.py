import json
from os import path
from pathlib import Path

from metrics import accuracy
from model import predict_label

"""
eval.py
Reads data.json file.
Used the model to predict labels.
Calculates accuracy.
Prints results and saves a small JSON report.


"""

def load_data(file_path: str):
    """
    Docstring for load_data
    
    :param file_path: Description
    :type file_path: str
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data 

def main():
    #1 Paths

    data_path = Path(__file__).parent / "data.json"
    report_path = Path(__file__).parent / "report.json" 

    #2 Load data
    data = load_data(str(data_path))

    texts = [item['text'] for item in data]
    true_label = [item['label'] for item in data]

    #Predict labels
    pred_label = []
    for text in texts:
        pred = predict_label(text)
        pred_label.append(pred)

    #4 Calculate accuracy
    acc = accuracy(pred_label,true_label)    

    #5 print resulrs
    print(f"Number of samples: {len(data)}")
    print(f"Accuracy: {acc:.4f}")

    #6 Json report
    report = {
        "num_samples": len(data),
        "accuracy": acc,
        "tool": "toy3_json_eval",
        "true_labels": true_label,
        "predict_labels": pred_label

    }

    with open(report_path, 'w') as f:
        json.dump(report, f, indent=4)
    print(f"report saaved to {report_path}")

main()         
    
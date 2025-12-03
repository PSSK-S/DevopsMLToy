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
    data = load_data(data_path)
    

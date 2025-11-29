#devopsMl_

import sys
from transformers import pipeline

def main():

    examples = [  "I love how simple HuggingFace pipelines are!",
        "This is the worst project I’ve ever worked on.",
        "The weather is okay but could be better.",
        "I'm excited to build DevOpsML!",
        "Ugh… I hate waiting for slow CI/CD pipelines."]
    
    nlp = pipeline("text-classification", model='distilbert-base-uncased-finetuned-sst-2-english')

    for i, text in enumerate(examples, start=1):
        result = nlp(text)
        print(result)

#main()        


def main2():    
    qa = pipeline("question-answering", model='distilbert-base-uncased-distilled-squad') 
    context = "I am from Amalapuram, a city in the Indian state of Andhra Pradesh. It is known for its rich cultural heritage and historical significance " \
    "as well as its beautiful landscapes and vibrant festivals. My favorite food is Chikkudukaya curry which my mom makes."

    question = ["What is the state mentioned in the context?",
                "What is the favorite food mentioned in the context?",
                "who makes the curry?"]
    
    for q in question:
        res = qa(question=q, context=context)
        print(res)

main2()
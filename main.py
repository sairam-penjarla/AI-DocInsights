from transformers import pipeline
import pytesseract
import yaml
from utils import load_config

# Load configuration
config = load_config("config.yaml")

# Load the model
nlp = pipeline(
    "document-question-answering",
    model=config['model']['name'],
)

# List of documents and corresponding questions
documents = [
    {"url": "https://templates.invoicehome.com/invoice-template-us-neat-750px.png", "question": "What is the invoice number?"},
    {"url": "https://miro.medium.com/max/787/1*iECQRIiOGTmEFLdWkVIH2g.jpeg", "question": "What is the purchase amount?"},
    {"url": "https://www.accountingcoach.com/wp-content/uploads/2013/10/income-statement-example@2x.png", "question": "What are the 2020 net sales?"},
]

# Process each document and print the result
for doc in documents:
    answer = nlp(doc["url"], doc["question"])
    print(f"Question: {doc['question']}\nAnswer: {answer['answer']}\nScore: {answer['score']:.4f}\n")

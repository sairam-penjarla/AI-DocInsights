# AI-DocInsight

## Description

AI-DocInsights is a simple Generative AI project that leverages a pre-trained model to answer questions based on document images. The model can process document images like invoices, receipts, and financial statements, providing specific answers to user queries.

## Setup

### Step 1: Clone the Repository

First, clone the project repository from GitHub:

```bash
git clone https://github.com/sairam-penjarla/AI-DocInsights.git
cd AI-DocInsights
```

### Step 2: Install the Required Dependencies

Navigate to the project directory and install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### Step 3: Install Tesseract OCR

Tesseract OCR is required for the `pytesseract` library to perform optical character recognition on the images. Install it by running:

```bash
sudo apt install tesseract-ocr
```

### Step 4: Run the Script

Now, run the main script:

```bash
python main.py
```

This will load the pre-trained model and process the specified documents, outputting the answers to the questions provided.

## Configuration

The model name is configured in `config.yaml`. You can change the model by updating the value in the YAML file.

## Usage

This project demonstrates how to use a pre-trained Generative AI model for document question answering. You can easily extend this project to other use cases by modifying the document URLs and questions in `main.py`.
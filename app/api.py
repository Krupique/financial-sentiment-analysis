from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import uvicorn

# Create an instance of FastAPI application
app = FastAPI()

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("model/finbert_tokenizer")
# Load model
llm_model = AutoModelForSequenceClassification.from_pretrained("model/finbert_model")

# Set the class Item using Pydantic to data validation
class Item(BaseModel):
    text: str
    title: str


# Set the async function to predict the sentiment
async def sentiment_predict(input_text):

    # Tokenize the input text
    inputs = tokenizer(input_text, 
                       return_tensors = "pt", 
                       truncation = True, 
                       padding = True, 
                       max_length = 512)

    # Do the prediction without calculate the grads
    with torch.no_grad():
        outputs = llm_model(**inputs)

    # Calculate the probabilities of predictions
    preds_probs = torch.softmax(outputs.logits, dim=1).squeeze().tolist()

    return preds_probs
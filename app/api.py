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

# Set the root path that returns a simple message
@app.get("/")
def index():
    return {"AI App using LLM to analyze the sentiment in Financial News"}


# Set the path to analyze the sentiment which allows POST requests
@app.post("/dsa_analisa_sentimento/")
async def dsa_analisa_sentimento(item: Item):

    # Concatenate the title and the text of the input item
    input_text = item.title + " " + item.text

    # Get the probabilities predictions
    preds_probs = await sentiment_predict(input_text)

    # Mpa the index of probabilities for the sentiments
    dsa_sentimento_mapping = {0: "Negative", 1: "Neutral", 2: "Positive"}

    # Get the predicted sentiment based on maximum likelihood
    predicted_sentiment = dsa_sentimento_mapping[preds_probs.index(max(preds_probs))]
    
    # Creates the response body with predicted sentiment and probabilities
    response_body = {
        "predicted_sentiment": predicted_sentiment,
        "prediction_probabilities": {
            "Negative": preds_probs[0],
            "Neutral": preds_probs[1],
            "Positive": preds_probs[2]
        }
    }
    
    return response_body
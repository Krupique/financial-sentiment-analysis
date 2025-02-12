
# Sentiment Analysis Project with FinBERT

## Overview

This project uses a pre-trained language model, FinBERT, to classify financial news into three sentiment categories: **Positive**, **Neutral**, and **Negative**. The system consists of an API built with FastAPI, which serves the model, and a client that makes requests to the API to obtain sentiment predictions.

The project structure is as follows:

```
fin-analysis/
├── app/
│   ├── api.py
│   └── client.py
├── data/
│   └── news.json
├── model/
│   ├── finbert_model/
│   └── finbert_tokenizer/
├── Dockerfile
├── .gitignore
├── poetry.lock
├── pyproject.toml
└── README.md
```

---

## Requirements

- Python 3.12 or higher
- Docker (optional, for running the API in a container)
- Poetry (for dependency management)

---

## Environment Setup

### 1. Installing Dependencies

The project uses Poetry to manage dependencies. To install the dependencies, run the following command in the project's root directory:

```bash
poetry install
```

### 2. Downloading the FinBERT Model

The FinBERT model and its tokenizer should already be downloaded and located in the `model/` folder. Ensure that the directories `finbert_model/` and `finbert_tokenizer/` are present.

---

## Running the API

The API is built with FastAPI and can be run directly or in a Docker container.

### Running Locally

To run the API locally, execute the following command:

```bash
poetry run python app/api.py
```

The API will be available at `http://127.0.0.1:8787`.

### Running with Docker

1. Build the Docker image:

    ```bash
    docker build -t finbert-api .
    ```

2. Run the container:

    ```bash
    docker run -p 8787:8787 finbert-api
    ```

The API will be available at `http://127.0.0.1:8787`.

---

## Running the Client

The client (`client.py`) makes requests to the API to classify the sentiment of financial news. To run the client, ensure the API is running and execute:

```bash
poetry run python app/client.py
```

The client will read the `data/news.json` file, which should contain the title and text of the news to be analyzed. Example of `news.json`:

```json
{
    "title": "Company X reports record profits",
    "text": "Company X announced today that it has achieved record profits in the last quarter..."
}
```

---

## API Endpoints

### 1. **GET /**  
Returns a simple message indicating that the API is running.

**Example Response:**
```json
{
    "message": "AI App using LLM to analyze the sentiment in Financial News"
}
```

### 2. **POST /sentiment_analysis/**  
Receives a JSON with the title and text of a financial news article and returns the predicted sentiment.

**Request Body:**
```json
{
    "title": "Company X reports record profits",
    "text": "Company X announced today that it has achieved record profits in the last quarter..."
}
```

**Example Response:**
```json
{
    "predicted_sentiment": "Positive",
    "prediction_probabilities": {
        "Negative": 0.05,
        "Neutral": 0.15,
        "Positive": 0.80
    }
}
```

---

## Project Structure

- **app/api.py**: Contains the FastAPI application that serves the FinBERT model.
- **app/client.py**: Client that makes requests to the API to classify news sentiment.
- **data/news.json**: Input file containing the title and text of the news to be analyzed.
- **model/**: Contains the FinBERT model and tokenizer.
- **Dockerfile**: Configuration to run the API in a Docker container.
- **poetry.lock** and **pyproject.toml**: Poetry configuration files for dependency management.

---

## Example Usage

1. Start the API (locally or via Docker).
2. Run the client (`client.py`).
3. The client will send the news contained in `data/news.json` to the API and display the predicted sentiment and associated probabilities.

**Expected Output:**
```
Real-time financial news sentiment analysis using LLM, deployed via API with a client module for instant insights.

Text: Company X announced today that it has achieved record profits in the last quarter...

Predicted sentiment: Positive

Probabilities:
    Negative: 5.0%
    Neutral: 15.0%
    Positive: 80.0%
```

---

## Final Considerations

This project is a simple yet powerful application for sentiment analysis in financial news. It can be expanded to include more features, such as support for multiple languages, batch analysis of multiple news articles, or integration with real-time news sources.

For questions or suggestions, refer to the official documentation of [FastAPI](https://fastapi.tiangolo.com/) and [Hugging Face Transformers](https://huggingface.co/transformers/).

--- 

**Note**: Ensure that the `data/news.json` file is correctly formatted before running the client.
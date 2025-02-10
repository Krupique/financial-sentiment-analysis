# Import
import requests

# Defining the API endpoint
url = "http://127.0.0.1:8787/sentiment_analysis/"

# Define the payload (text and title)
payload = {
    "text": "Bank of Japan Reports Record Stock Gains for Last Financial Year.",
    "title": "Economy"
}

# Send a POST request to API endpoint
response = requests.post(url, json=payload)

# Verifying if the request was succesful (status code 200)
if response.status_code == 200:
    # Get the content of the answer (sentiment and probabilities predicted)
    response_data = response.json()

    predicted_sentiment = response_data.get('predicted_sentiment')
    probabilities = response_data.get('prediction_probabilities')

    # Print
    print("Real-time financial news sentiment analysis using LLM, deployed via API with a client module for instant insights.")

    # Analyzed text
    print("\nText: {}".format(payload["text"]))
    print("\nPredicted sentiment: {}".format(predicted_sentiment))
    print("\nProbabilities:")

    for sentiment, prob in probabilities.items():
        perc = round(prob * 100, 2)
        print("\t{}: {}%".format(sentiment, perc))

else:
    print('Error: {}'.format(response.text))
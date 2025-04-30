import pandas as pd
import requests
import nltk
from google.cloud import bigquery
from google.oauth2 import service_account
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon for sentiment analysis if not already present
nltk.download('vader_lexicon')

# Define a function to fetch data from SuiteCRM REST API
def fetch_data_from_api():
    # Define the API endpoint and headers
    api_url = "https://suitecrm.example.com/api/v1/reviews"  # Replace with the actual SuiteCRM API endpoint
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",  # Replace with your SuiteCRM access token
        "Content-Type": "application/json"
    }

    # Make a GET request to the API
    response = requests.get(api_url, headers=headers)

    # Check for a successful response
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        # Convert the JSON response into a DataFrame
        df = pd.DataFrame(data['records'])  # Adjust based on the actual response structure
        return df
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

# Fetch the customer reviews data using the REST API
customer_reviews_df = fetch_data_from_api()

# Ensure ReviewText is a string and handle missing values
customer_reviews_df['ReviewText'] = customer_reviews_df['ReviewText'].fillna('').astype(str)

# Path to your Google Cloud service account key JSON file
service_account_path = r'D:\SUNNY\Career\BI Projects Explaination - Hexis, HCM, APAC\Marketing Analytics Dashboard\Marketing Analytics Main Project\marketing-analytics-445211-0450fd9f661d.json'

# Set project and dataset details
project_id = "marketing-analytics-445211"
dataset_id = "Marketing_Analytics"
table_name = "fact_customer_reviews_with_sentiment"

# Initialize the VADER sentiment intensity analyzer
sia = SentimentIntensityAnalyzer()

# Define a function to calculate sentiment scores using VADER
def calculate_sentiment(review):
    sentiment = sia.polarity_scores(review)
    return sentiment['compound']

# Define a function to categorize sentiment using both the sentiment score and the review rating
def categorize_sentiment(score, rating):
    if score > 0.05:  # Positive sentiment score
        if rating >= 4:
            return 'Positive'
        elif rating == 3:
            return 'Mixed Positive'
        else:
            return 'Mixed Negative'
    elif score < -0.05:  # Negative sentiment score
        if rating <= 2:
            return 'Negative'
        elif rating == 3:
            return 'Mixed Negative'
        else:
            return 'Mixed Positive'
    else:  # Neutral sentiment score
        if rating >= 4:
            return 'Positive'
        elif rating <= 2:
            return 'Negative'
        else:
            return 'Neutral'

# Define a function to bucket sentiment scores into text ranges
def sentiment_bucket(score):
    if score >= 0.5:
        return '0.5 to 1.0'
    elif 0.0 <= score < 0.5:
        return '0.0 to 0.49'
    elif -0.5 <= score < 0.0:
        return '-0.49 to 0.0'
    else:
        return '-1.0 to -0.5'

# Apply sentiment analysis
customer_reviews_df['SentimentScore'] = customer_reviews_df['ReviewText'].apply(calculate_sentiment)
customer_reviews_df['SentimentCategory'] = customer_reviews_df.apply(
    lambda row: categorize_sentiment(row['SentimentScore'], row['Rating']), axis=1)
customer_reviews_df['SentimentBucket'] = customer_reviews_df['SentimentScore'].apply(sentiment_bucket)

# Upload the analyzed data to BigQuery
def upload_to_bigquery(df, project_id, dataset_id, table_name, service_account_path):
    credentials = service_account.Credentials.from_service_account_file(service_account_path)
    client = bigquery.Client(credentials=credentials, project=project_id)
    
    table_id = f"{project_id}.{dataset_id}.{table_name}"
    
    # Define the BigQuery job configuration
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE  # Replace table if it exists
    )
    
    # Load data to BigQuery
    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()  # Wait for the job to complete
    
    print(f"Data successfully loaded to BigQuery table: {table_id}")

# Call the function to upload data
upload_to_bigquery(customer_reviews_df, project_id, dataset_id, table_name, service_account_path)

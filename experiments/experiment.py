#used python 3.10 for smootly running tweepy
import requests
import time
from datetime import datetime

# Mockoon Twitter v2 API configuration
MOCK_API_URL = "http://localhost:3000"
MOCK_BEARER_TOKEN = "mock_bearer_token_123"  # This can be any value for Mockoon

class TweetReach:
    def __init__(self):
        self.base_url = MOCK_API_URL
        self.headers = {
            "Authorization": f"Bearer {MOCK_BEARER_TOKEN}",
            "Content-Type": "application/json"
        }
        self.search_terms = [
            "#python", 
            "#datascience", 
            "#machinelearning", 
            "#ai", 
            "#pythonjobs", 
            "#mljobs", 
            "#techjobs", 
            "#coding", 
            "#programming", 
            "#artificialintelligence",
            "#deeplearning",
            "#pythondeveloper",
            "#datascientist",
            "#aiengineer"
        ]

    def on_connect(self):
        print("Connected to Mockoon Twitter v2 API :)")

    def on_tweet(self, tweet):
        print(f"\nTweet received at {datetime.now()}")
        print(f"Text: {tweet.get('text', 'No text')}")
        if 'author_id' in tweet:
            print(f"Author ID: {tweet['author_id']}")
        print("-" * 50)

    def start_streaming(self):
        self.on_connect()
        print("Starting to fetch tweets...")
        
        for term in self.search_terms:
            try:
                # Make request to Mockoon Twitter v2 API
                endpoint = f"/2/tweets/search/recent?query={term}"
                response = requests.get(
                    f"{self.base_url}{endpoint}",
                    headers=self.headers
                )
                
                if response.status_code == 200:
                    data = response.json()
                    if 'data' in data:
                        print(f"\nFound {len(data['data'])} tweets for {term}")
                        for tweet in data['data']:
                            self.on_tweet(tweet)
                    else:
                        print(f"No tweets found for {term}")
                else:
                    print(f"Error: Received status code {response.status_code} for term {term}")
                
                # Add delay to simulate real-time streaming
                time.sleep(2)
                
            except requests.exceptions.ConnectionError:
                print("Error: Could not connect to Mockoon server. Make sure it's running on port 3000")
                break
            except Exception as e:
                print(f"Error processing term {term}: {str(e)}")

if __name__ == '__main__':
    print("Starting TweetReach with Mockoon Twitter v2 API...")
    stream = TweetReach()
    stream.start_streaming()
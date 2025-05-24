import requests
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from collections import defaultdict
import threading
import os
from dotenv import load_dotenv
load_dotenv()

# Mockoon Twitter v2 API configuration
MOCK_API_URL = "http://localhost:3000"
MOCK_BEARER_TOKEN = "mock_bearer_token_123"

# Email configuration
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("APP_PASSWORD")  # Using the same app password from email_experiment.py
EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT")

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
        self.tweet_buffer = defaultdict(list)
        
        # Start email timer
        self.email_timer = threading.Timer(10, self.send_periodic_email)
        self.email_timer.daemon = True
        self.email_timer.start()

    def on_connect(self):
        print("Connected to Mockoon Twitter v2 API :)")

    def on_tweet(self, tweet, keyword):
        print(f"\nTweet received at {datetime.now()}")
        print(f"Text: {tweet.get('text', 'No text')}")
        if 'author_id' in tweet:
            print(f"Author ID: {tweet['author_id']}")
        print("-" * 50)
        
        # Add tweet to buffer
        self.tweet_buffer[keyword].append(tweet)

    def send_periodic_email(self):
        try:
            # Create email content
            subject = f"Tweets Update - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            message = "Tweets collected in the last 10 seconds:\n\n"

            for keyword, tweets in self.tweet_buffer.items():
                if tweets:
                    message += f"=== {keyword} ===\n"
                    message += f"Found {len(tweets)} tweets:\n\n"
                    
                    for tweet in tweets:
                        message += f"Tweet: {tweet.get('text', 'No text')}\n"
                        message += f"Author ID: {tweet.get('author_id', 'Unknown')}\n"
                        message += f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                        message += "-" * 50 + "\n"

            # Format email
            text = f"Subject: {subject}\n\n{message}"

            # Send email using simpler approach
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECIPIENT, text)
            server.quit()

            print(f"Periodic email sent at {datetime.now()}")
            
            # Clear the buffer after sending
            self.tweet_buffer.clear()
            
            # Reset the timer for next 10 seconds
            self.email_timer = threading.Timer(10, self.send_periodic_email)
            self.email_timer.daemon = True
            self.email_timer.start()

        except Exception as e:
            print(f"Error sending email: {str(e)}")

    def start_streaming(self):
        self.on_connect()
        print("Starting to fetch tweets...")
        print("Emails will be sent every 10 seconds...")
        
        while True:  # Continuous streaming
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
                                self.on_tweet(tweet, term)
                        else:
                            print(f"No tweets found for {term}")
                    else:
                        print(f"Error: Received status code {response.status_code} for term {term}")
                    
                    # Add delay to simulate real-time streaming
                    time.sleep(1)
                    
                except requests.exceptions.ConnectionError:
                    print("Error: Could not connect to Mockoon server. Make sure it's running on port 3000")
                    break
                except Exception as e:
                    print(f"Error processing term {term}: {str(e)}")

if __name__ == '__main__':
    print("Starting TweetReach with Mockoon Twitter v2 API...")
    stream = TweetReach()
    stream.start_streaming()
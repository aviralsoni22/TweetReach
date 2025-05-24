import requests, time, threading
from datetime import datetime
from collections import defaultdict
from src.tweet_reach.utils.email_sender import send_email
from src.tweet_reach.config.settings import *

class TweetReach:
    def __init__(self):
        self.base_url = MOCK_API_URL
        self.headers = {"Authorization": f"Bearer {MOCK_BEARER_TOKEN}"}
        self.search_terms = ["#datascience", "#pythonjobs", "#ai"]  # trimmed
        self.tweet_buffer = defaultdict(list)
        self.email_timer = threading.Timer(10, self.send_periodic_email)
        self.email_timer.daemon = True
        self.email_timer.start()

    def on_connect(self): print("Connected to Mock API")

    def on_tweet(self, tweet, keyword):
        print(f"\n[{datetime.now()}] {keyword}: {tweet.get('text')}")
        self.tweet_buffer[keyword].append(tweet)

    def send_periodic_email(self):
        subject = f"Tweet Alerts - {datetime.now():%Y-%m-%d %H:%M}"
        message = ""
        for kw, tweets in self.tweet_buffer.items():
            message += f"\n=== {kw} ({len(tweets)}) ===\n"
            for t in tweets:
                message += f"{t.get('text')}\nAuthor: {t.get('author_id', 'N/A')}\n---\n"
        send_email(subject, message, EMAIL_SENDER, EMAIL_RECIPIENT, EMAIL_PASSWORD)
        self.tweet_buffer.clear()
        self.email_timer = threading.Timer(10, self.send_periodic_email)
        self.email_timer.daemon = True
        self.email_timer.start()

    def start_streaming(self):
        self.on_connect()
        while True:
            for term in self.search_terms:
                try:
                    res = requests.get(f"{self.base_url}/2/tweets/search/recent?query={term}", headers=self.headers)
                    if res.status_code == 200 and "data" in res.json():
                        for tweet in res.json()["data"]:
                            self.on_tweet(tweet, term)
                    time.sleep(1)
                except Exception as e:
                    print(f"Error: {e}")

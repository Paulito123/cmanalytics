from dotenv import load_dotenv
import tweepy
import os

load_dotenv()

client = tweepy.Client(bearer_token=f'{os.getenv("TWITTER_API_BEARER")}')

# Replace with your own search query
query = 'parsiq -is:retweet OR prq -is:retweet'

counts = client.get_recent_tweets_count(query=query, granularity='day')

for count in counts.data:
    print(count)

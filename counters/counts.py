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

# {'end': '2022-07-31T00:00:00.000Z', 'start': '2022-07-30T03:42:36.000Z', 'tweet_count': 123}
# {'end': '2022-08-01T00:00:00.000Z', 'start': '2022-07-31T00:00:00.000Z', 'tweet_count': 171}
# {'end': '2022-08-02T00:00:00.000Z', 'start': '2022-08-01T00:00:00.000Z', 'tweet_count': 190}
# {'end': '2022-08-03T00:00:00.000Z', 'start': '2022-08-02T00:00:00.000Z', 'tweet_count': 277}
# {'end': '2022-08-04T00:00:00.000Z', 'start': '2022-08-03T00:00:00.000Z', 'tweet_count': 133}
# {'end': '2022-08-05T00:00:00.000Z', 'start': '2022-08-04T00:00:00.000Z', 'tweet_count': 107}
# {'end': '2022-08-06T00:00:00.000Z', 'start': '2022-08-05T00:00:00.000Z', 'tweet_count': 217}
# {'end': '2022-08-06T03:42:36.000Z', 'start': '2022-08-06T00:00:00.000Z', 'tweet_count': 9}

# {'end': '2022-07-31T00:00:00.000Z', 'start': '2022-07-30T03:55:38.000Z', 'tweet_count': 778}
# {'end': '2022-08-01T00:00:00.000Z', 'start': '2022-07-31T00:00:00.000Z', 'tweet_count': 935}
# {'end': '2022-08-02T00:00:00.000Z', 'start': '2022-08-01T00:00:00.000Z', 'tweet_count': 1067}
# {'end': '2022-08-03T00:00:00.000Z', 'start': '2022-08-02T00:00:00.000Z', 'tweet_count': 1031}
# {'end': '2022-08-04T00:00:00.000Z', 'start': '2022-08-03T00:00:00.000Z', 'tweet_count': 1042}
# {'end': '2022-08-05T00:00:00.000Z', 'start': '2022-08-04T00:00:00.000Z', 'tweet_count': 925}
# {'end': '2022-08-06T00:00:00.000Z', 'start': '2022-08-05T00:00:00.000Z', 'tweet_count': 1002}
# {'end': '2022-08-06T03:55:38.000Z', 'start': '2022-08-06T00:00:00.000Z', 'tweet_count': 162}

# {'end': '2022-07-31T00:00:00.000Z', 'start': '2022-07-30T04:01:34.000Z', 'tweet_count': 1076}
# {'end': '2022-08-01T00:00:00.000Z', 'start': '2022-07-31T00:00:00.000Z', 'tweet_count': 1282}
# {'end': '2022-08-02T00:00:00.000Z', 'start': '2022-08-01T00:00:00.000Z', 'tweet_count': 1602}
# {'end': '2022-08-03T00:00:00.000Z', 'start': '2022-08-02T00:00:00.000Z', 'tweet_count': 2729}
# {'end': '2022-08-04T00:00:00.000Z', 'start': '2022-08-03T00:00:00.000Z', 'tweet_count': 3714}
# {'end': '2022-08-05T00:00:00.000Z', 'start': '2022-08-04T00:00:00.000Z', 'tweet_count': 1091}
# {'end': '2022-08-06T00:00:00.000Z', 'start': '2022-08-05T00:00:00.000Z', 'tweet_count': 1386}
# {'end': '2022-08-06T04:01:34.000Z', 'start': '2022-08-06T00:00:00.000Z', 'tweet_count': 183}
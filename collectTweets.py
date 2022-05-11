import tweepy
import json
from pprint import pprint
import time
import csv

with open('package.json', 'r') as file:
    keys = json.load(file)

client = tweepy.Client(bearer_token=keys['Bearer_Token'])

with open('leftwingaccounts.txt', 'r') as file:
    accounts = file.read().split('\n')

with open('tweets.csv', 'w', newline='', encoding='utf8') as file:
    writer = csv.writer(file)
    for user in accounts:
        user = client.get_user(username=user)
        if user is None:
            continue
        user = user.data.data
        likedTweets = client.get_liked_tweets(user['id'])
        tweets = client.get_users_tweets(user['id'])
        for tweet in likedTweets.data:
            writer.writerow([tweet.text])
        for tweet in tweets.data:
            writer.writerow([tweet.text])

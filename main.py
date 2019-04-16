#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import gpt_tweet

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'b5sMlO6miMiZbfOz32SEUtxSK'
CONSUMER_SECRET = 'JyY4qOEE9oXuxtBGT0FiryMfCw6DRtIvxIthETCHkhjKjcDBm5'
ACCESS_KEY = '1097875655209959425-EmyQwvu9Q5GJgY8NIVKiWwWbXrktJf'
ACCESS_SECRET = 'a5lfF9Hfri0rxe7FMEeyUE1pv4at1unMlwLBAkmQlQND9'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

class twitterData():

    def _init_(self, user, tweetContent, id):
        self.user = 'user'
        self.tweetContent = 'tweetContent'
        self.tweetid = 0

class listener(StreamListener):

    def on_data(self, data):
        json_data = json.loads(data)
        twitterData.user = json_data['user']['screen_name']
        twitterData.tweetContent = json_data['text']
        twitterData.id = json_data['id']
        print(twitterData.user)
        print(twitterData.tweetContent)
        gpt_tweet.tweet_response(twitterData.user, twitterData.tweetContent)
        return(True)

    def on_error(self, status):
        print(status)


twitterStream = Stream(auth, listener())
twitterStream.filter(track=["@gpt2bot"])


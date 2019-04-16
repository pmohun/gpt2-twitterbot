#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, boto3
from os import environ

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

import smart_open
def read_samples():
    filename = smart_open.smart_open('s3://gpt2-samples/gpt2-samples.txt','rb')
    f=filename.readlines()
    filename.close()
    sleep = 60 * 60; # 1 hour interval
    return f

def tweet_response(mention):
    api.update_status(mention)

def tweet_sample(f):
    for line in f:
        # check to see if we can post without hitting twitter's character limit
        if len(line) < 280:
            # ignore lines that consist only of spaces
            if len(line) == 1:
                new_line = ''
                pass
            else:
            # update the status with the line from the sample text 
                new_line = line
                try: 
                    api.update_status(new_line)
                    time.sleep(sleep) #Tweet every x minutes
                except:
                    print('Short line exception.')
                    pass
        else:   
            i = 0
            for i in range(0,280):
                try:
                    new_line += line[i]
                    i += 1
                except:
                    print('Int to byte error')
            try:
                api.update_status(new_line)
                num_replies = round(line/280)
                time.sleep(sleep) #Tweet every x minutes
            except:
                print('Large line exception.')
                pass
    
if __name__ == "__main__":
    samples = read_samples()
    tweet_sample(samples)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
from os import environ

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()
sleep = 60 * 60; # 1 hour interval
i = 1
while i > 0:
    new_line = i
    api .update_status(str(new_line)
    i + 1
    time.sleep(sleep)

'''for line in f:
    if len(line) < 280:
        if len(line) == 1:
            new_line = ''
            pass
        else:
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
            new_line += line[i]
            i += 1
        try:
            api.update_status(new_line)
            num_replies = round(line/280)
            time.sleep(sleep) #Tweet every x minutes
        except:
            print('Large line exception.')
            pass
'''
    

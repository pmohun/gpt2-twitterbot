import tweepy, time, sys, re
import build_text

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'b5sMlO6miMiZbfOz32SEUtxSK'
CONSUMER_SECRET = 'JyY4qOEE9oXuxtBGT0FiryMfCw6DRtIvxIthETCHkhjKjcDBm5'
ACCESS_KEY = '1097875655209959425-EmyQwvu9Q5GJgY8NIVKiWwWbXrktJf'
ACCESS_SECRET = 'a5lfF9Hfri0rxe7FMEeyUE1pv4at1unMlwLBAkmQlQND9'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def compose_tweet(prompt):
    gpt_text = build_text.interact_model(prompt = "mention")
    # Remove any truncated text from beginning of prompt
    m = re.search(r'\r\n|\r|\n', gpt_text)
    print(m.group(0))




'''
def tweet_response(user, mention):
    gpt_text = build_text.interact_model(prompt = "mention")
    tweet = ''
    # Twitter allows 280 character updates, not including the username & '@' symbol
    char_limit = 278 - len(user)
    for i in range(0,char_limit):
        tweet += gpt_text[i]
    api.update_status('@' + user + ' ' + tweet)

'''
if __name__ == '__main__':
    prompt = input()
    compose_tweet(prompt)


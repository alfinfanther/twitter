import tweepy
from tweepy import OAuthHandler
# http://pydoc.net/tweepy/3.1.0/examples.streaming/
consumer_key = 'xxx'
consumer_secret = 'xxxx'
access_token = 'xxxx'
access_secret = 'xxxx'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


def g_status():
    for status in tweepy.Cursor(api.home_timeline).items(10):
        print (status)

def g_trend():
    # tr = api.trends_available()
    tr = api.trends_place('23424846')
    for x in tr:
        for y in x['trends']:
            print(y)

def g_tag():
    se = api.search('#EkonomiDigital')
    print(se)

g_trend()



import os
import tweepy
class Tweet():
    def __init__(self, tweet_media, tweet_text):
        self.text = tweet_text
        self.media = tweet_media

    def post(self, api):
        print(self.media)
        api.update_with_media(filename = self.media, status = self.text)
        #return status.id

import os

class Tweet():
    def __init__(self, tweet_media, tweet_text):
        self.text = tweet_text
        self.media = tweet_media

    def post(self, api):
        status = api.update(filename = self.media, status = self.text)
        return status.id

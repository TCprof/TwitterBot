import os
import tweepy
import configparser

filepath = os.path.abspath(__file__)
name = os.path.dirname(filepath)

config = configparser.ConfigParser()
config.read(name + '/keys')
reddit_config = config['Reddit']
client_id = reddit_config['client_id']
client_secret = reddit_config['client_secret']
user_agent = reddit_config["client_secret"]

twitter_config = config['Twitter']
api_key = twitter_config['api_key']
secret = twitter_config['secret']
access_token = twitter_config['access_token']
token_secret = twitter_config['token_secret']

authentication = tweepy.OAuthHandler(api_key,secret)
authentication.set_access_token(access_token,token_secret)
api = tweepy.API(authentication)



import os
import random
import tweepy

from bot import Media
from settings import config

#returns a list of images from a folder
def get_images(image_folder):
    img_list = []
    for dirpath, dirnames, files in os.walk(image_folder):
        for f in files:
            img_list.append(os.path.join(dirpath,f))
    return img_list

#gets image from list, tweets it and then deletes it
def tweet_image(img_list):
    img = random.choice(img_list)
    try:
        t = Media.Tweet(img,"test")
        t.post(api)
    except tweepy.error.TweepError:
        print("This image could not be read")
    os.remove(img)


def main():
    global api
    api = config.api
    tweet_image(get_images('pics'))

if __name__ == "__main__":
    main()





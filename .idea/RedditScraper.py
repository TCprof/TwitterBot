import praw
import shutil
import requests
import urllib
import os

image_dir = 'pics'
image_extentions = ['.jpg','.jpeg','.png']

class RedditScraper:
    def __init__(self, client_id, client_secret, user_agent, subreddits_list, limit):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent
        self.subreddits_list = subreddits_list
        self.limit = limit
        self.bot = praw.Reddit(client_id=self.client_id,client_secret=self.client_secret,user_agent=self.user_agent)
        print("Reddit Image Scan Bot Initialized!")

    def collect_img(self):
        #self.all = self.reddit.subreddit('nocontextpics').top(limit=10)
        print('collecting data...')
        image_extentions = ['.jpg','.jpeg','.png']
        for subreddit_name in self.subreddits_list:
            self.image_urls = []
            self.image_ids = []
            subreddit = self.bot.subreddit(subreddit_name)
            posts = subreddit.hot(limit = self.limit)
            for post in posts:
                _, ext = os.path.splitext(post.url)
                if ext in image_extentions:
                    self.image_urls.append(post.url)
                    self.image_ids.append(post.id)
            self.save(subreddit=subreddit_name)

    def save(self, subreddit):
        print('Writing data to disk..')
        image_extentions = ['.jpg','.jpeg','.png']
        dirpath = os.path.join('./', subreddit)
        if not os.path.exists(dirpath):
            os.mkdir(dirpath)

        if(len(self.image_ids) > 0):
            images_path = os.path.join(dirpath, 'images/')
            if not os.path.exists(images_path):
                os.mkdir(images_path)

        for index, url in enumerate(self.image_urls):
            _, ext = os.path.splitext(url)
            print(str(self.image_urls[index]))
            if ext in image_extentions:
                try:
                    print ('downloading', self.image_urls[index])
                    urllib.request.urlretrieve(self.image_urls[index], images_path + self.image_ids[index] + ext)
                except:
                    print('something went wrong while downloading this', self.image_urls[index])
        print('finished writing data')

if __name__ == "__main__":
    reddit_bot = RedditScraper(my_client_id,my_client_secret,my_user_agent,['nocontextpics', 'pics'], 3)
    reddit_bot.collect_img()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from environment import theEmail, thePassword
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        print('The Bot is Online!')
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(1)
        email = bot.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        password = bot.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        login_button = bot.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        print('{} sent as email.'.format(self.username))
        password.send_keys(self.password)
        print('{} sent as password.'.format(self.password))
        login_button.click()
        time.sleep(3)

    def Tweetting(self):
        def tweetMaker():
            moviesDB = pd.read_csv("movies.csv", encoding="utf-8", delimiter=';')
            original_title = moviesDB["original_title"]
            director = moviesDB["director"]
            genres = moviesDB["genre"]
            tt = moviesDB["imdb_title_id"]
            year = moviesDB["year"]
            duration = moviesDB["duration"]

            def getRandom():
                i = random.randint(0, 2019)
                film = [original_title[i], year[i], director[i], genres[i], duration[i], tt[i]]
                return film

            def getRating(tt):
                url = "https://www.imdb.com/title/"+tt
                r = requests.get(url)
                soup = BeautifulSoup(r.content, "html.parser")
                rating = soup.find_all("span", {"itemprop": "ratingValue"})
                rating = rating[0].text
                return rating

            film = getRandom()
            ttid = film[5]
            rating = getRating(ttid)
            tweet = "{} | Yıl: {} | IMDb: {}\nYön: {}\nTür: {}\n{}dk\n#sinema #film #öneri\nhttps://www.imdb.com/title/{}".format(film[0], film[1], rating, film[2], film[3], film[4], film[5])

            if len(tweet) >= 275:
                return tweetMaker()
            else:
                return tweet
        bot = self.bot
        tweet_button = bot.find_element_by_xpath('/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet_button.click()
        time.sleep(1)
        tweet_area = bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
        tweet_area.clear()
        theTweet = tweetMaker()
        tweet_area.send_keys(theTweet)
        time.sleep(1)
        tweet_send_button = bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        tweet_send_button.click()
        print('"{}" sent as Tweet.'.format(theTweet))
            

theEmail = theEmail()
thePassword = thePassword()
cengizentel = TwitterBot(theEmail, thePassword)
cengizentel.login()

while True:
    cengizentel.Tweetting()
    time.sleep(10800)
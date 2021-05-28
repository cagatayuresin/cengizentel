from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from environment import theEmail, thePassword
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
import datetime

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
                rating = soup.find_all("span", {"class": "AggregateRatingButton__RatingScore-sc-1il8omz-1 fhMjqK"})
                try:
                    rating = rating[0].text
                except IndexError:
                    rating = "Null"
                return rating
                
            film = getRandom()
            ttid = film[5]
            rating = getRating(ttid)
            tweet = "{} || {} || IMDb: {}\n{}\n{}\n{}min\n#sinema #film #öneri #movie #cinema\nhttps://www.imdb.com/title/{}".format(film[0], film[1], rating, film[2], film[3], film[4], film[5])
            if len(tweet) >= 275:
                return tweetMaker()
            else:
                return tweet
                
        bot = self.bot
        tweet_button = bot.find_element_by_xpath('/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet_button.click()
        time.sleep(3)
        tweet_area = bot.find_element_by_css_selector(".r-1dqxon3 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)")
        tweet_area.click()
        theTweet = tweetMaker()
        tweet_area.send_keys(theTweet)
        time.sleep(1)
        tweet_send_button = bot.find_element_by_css_selector('html body div#react-root div.css-1dbjc4n.r-13awgt0.r-12vffkv div.css-1dbjc4n.r-13awgt0.r-12vffkv div#layers.r-1d2f490.r-u8s1d.r-zchlnj.r-ipm5af.r-184en5c div.css-1dbjc4n.r-aqfbo4.r-1d2f490.r-12vffkv.r-1xcajam.r-zchlnj div.css-1dbjc4n.r-12vffkv div.css-1dbjc4n.r-12vffkv div.css-1dbjc4n.r-1p0dtai.r-1adg3ll.r-1d2f490.r-bnwqim.r-zchlnj.r-ipm5af div.r-1oszu61.r-vqxq0j.r-1p0dtai.r-deolkf.r-1adg3ll.r-1mlwlqe.r-eqz5dr.r-1d2f490.r-crgep1.r-ifefl9.r-bcqeeo.r-t60dpp.r-bnwqim.r-zchlnj.r-ipm5af.r-417010 div.css-1dbjc4n.r-1pz39u2.r-16y2uox.r-1wbh5a2 div.css-1dbjc4n.r-1habvwh.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-rsyp9y.r-1pjcn9w.r-htvplk.r-1udh08x.r-1potc6q div.css-1dbjc4n.r-kemksi.r-1867qdf.r-16y2uox.r-1wbh5a2 div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu div.css-1dbjc4n.r-1pp923h.r-1moyyf3.r-16y2uox.r-1wbh5a2.r-1dqxon3 div.css-1dbjc4n.r-iphfwy div.css-1dbjc4n.r-kemksi.r-1pp923h.r-1moyyf3.r-oyd9sg div div.css-1dbjc4n div.css-1dbjc4n div.css-1dbjc4n.r-ymttw5 div.css-1dbjc4n.r-18u37iz div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t div div.css-1dbjc4n div.css-1dbjc4n.r-1awozwy.r-kemksi.r-18u37iz.r-1w6e6rj.r-1wtj0ep.r-id7aif.r-184en5c div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1s2bzr4 div.css-18t94o4.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-1w2pmg.r-19u6a5r.r-ero68b.r-1gg2371.r-1ny4l3l.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr div.css-901oao.r-1awozwy.r-jwli3a.r-6koalj.r-18u37iz.r-16y2uox.r-1qd0xha.r-a023e6.r-b88u0q.r-1777fci.r-rjixqe.r-dnmrzs.r-bcqeeo.r-q4m81j.r-qvutc0 span.css-901oao.css-16my406.css-bfa6kz.r-poiln3.r-bcqeeo.r-qvutc0 span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0')
        tweet_send_button.click()
        print('{}\n{}\n**************'.format(theTweet, datetime.datetime.now()))
        
theEmail = theEmail()
thePassword = thePassword()
cengizentel = TwitterBot(theEmail, thePassword)
cengizentel.login()

while True:
    cengizentel.Tweetting()
    time.sleep(10800)
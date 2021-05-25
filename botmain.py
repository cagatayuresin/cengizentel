#Author: Çağatay ÜRESİN
#https://www.twitter.com/cagatayuresin
#cagatayuresin@gmail.com
#https://cagatayuresin.github.io/cengizentel/

#Initilize the Seleniun module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Time module for delays
import time

#Recieving bot secrets
from environment import theEmail, thePassword

#Requests and BeautifulSoup to recieve and keep up to date IMDb ratings
import requests
from bs4 import BeautifulSoup

#Pandas module for CSV Databse funtions
import pandas as pd

#Random module to picking a movie from the database
import random

#Datetime module to printing the log time
import datetime


# Creating a Bot object
class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        #At this moment Firefox will start
        self.bot = webdriver.Firefox()
    
    #This login method to make our bot login into Twitter 
    def login(self):
        print('The Bot is Online!')
        bot = self.bot
        bot.get('https://twitter.com/login')
        
        #This delay keeps us from an exception
        time.sleep(1)

        #Theese lines give us the email and password inputs' paths 
        email = bot.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        password = bot.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        login_button = bot.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')

        #Make sure inputs are blank. Theese lines keeps us from an exception due to autofill scripts
        email.clear()
        password.clear()

        #Literaly we are writing our email/username and password, clicking the login button now
        email.send_keys(self.username)
        print('{} sent as email.'.format(self.username))
        password.send_keys(self.password)
        print('{} sent as password.'.format(self.password))
        login_button.click()

        #Just wait for the login about 3 seconds
        time.sleep(3)

    #This method is for making the tweeting loop easy
    def Tweetting(self):

        #Every loop we are making a new tweet with this method
        def tweetMaker():

            #Teese lines are getting an access for databse and making simple variables of them
            moviesDB = pd.read_csv("movies.csv", encoding="utf-8", delimiter=';')
            original_title = moviesDB["original_title"]
            director = moviesDB["director"]
            genres = moviesDB["genre"]
            tt = moviesDB["imdb_title_id"]
            year = moviesDB["year"]
            duration = moviesDB["duration"]

            #This method is picking a random movie's data into a list
            def getRandom():
                i = random.randint(0, 2019)
                film = [original_title[i], year[i], director[i], genres[i], duration[i], tt[i]]
                return film

            #This method creates a request for the chosen movie to get actual rating
            def getRating(tt):
                url = "https://www.imdb.com/title/"+tt

                #Get the chosen movie's IMDb page's source code 
                r = requests.get(url)

                #Parsing the source code for paths and contents
                soup = BeautifulSoup(r.content, "html.parser")

                #Getting the rating's html piece from the whole source code by showing the path
                rating = soup.find_all("span", {"itemprop": "ratingValue"})

                #This gives the html piece's content so it is the rating as a string at the moment
                rating = rating[0].text
                return rating

            #Theese 4 lines creates a Twitter post
            film = getRandom()
            ttid = film[5]
            rating = getRating(ttid)
            tweet = "{} || {} || IMDb: {}\n{}\n{}\n{}min\n#sinema #film #öneri #movie #cinema\nhttps://www.imdb.com/title/{}".format(film[0], film[1], rating, film[2], film[3], film[4], film[5])

            #Controls the tweet if it fits. A tweet's char limit is 280 but just in case for escaping from exceptions due to encoding problems.
            if len(tweet) >= 275:
                #If the tweet is larger then 275 this tries the whole procces again
                return tweetMaker()
            #If the tweet fits in 280 it is done!
            else:
                return tweet
        
        bot = self.bot
        #Find the tweeting buton by the path and click to open input popup
        tweet_button = bot.find_element_by_xpath('/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet_button.click()

        #Just give me a second to open the tweeting input popup
        time.sleep(1)

        #Finf the tweeting input and clear it just in case
        tweet_area = bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
        tweet_area.clear()

        #Create a tweet
        theTweet = tweetMaker()

        #Typing the tweet
        tweet_area.send_keys(theTweet)

        #Make sure the tweet has written
        time.sleep(1)

        #Find the sending button then click
        tweet_send_button = bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        tweet_send_button.click()

        #Print the tweet and the time into terminal
        print('{}\n{}\n**************'.format(theTweet, datetime.datetime.now()))
            
#Get the secrets
theEmail = theEmail()
thePassword = thePassword()

#Binding between our bot object and our bot's Twitter account
cengizentel = TwitterBot(theEmail, thePassword)

#Be online
cengizentel.login()

#The main tweeting loop
while True:
    cengizentel.Tweetting()
    time.sleep(10800)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import credentials


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.firefox

    def login(self):
        bot = self.bot
        bot.get('http://www.instagram.com.accounts/login')
        time.sleep(5)

        email = bot.find_element_by_name('username').send_keys(self.username)
        password = bot.find_element_by_name('password').send_keys(self.password)

        time.sleep(1)
        bot.find_element_by_name('password').send_keys(Keys.RETURN)

        time.sleep(3)

    def findMyFollowers(self, number_of_followers):
        bot = self.bot

        bot.get('https://www.instagram.com/creed_d_programmer/?hl=en')
        time.sleep(2)

        bot.find_element_by_xpath('//a[@href=/' + self.username + '/followers/').click()
        time.sleep(1)

        popup = bot.find_element_by_class_name('isgrP')

        followers_array = []

        i = 1
        while len(followers_array) <= number_of_followers:
            bot.execute('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
            time.sleep(0.4)

            followers = bot.find_element_by_class_name('FPmhX')

            for follower in followers:
                if follower not in followers_array:
                    followers_array.append(follower.text)

            i += 1
        print(followers_array)
        self.followers = followers_array


insta = InstagramBot('creed_d_programmer', 'temidayo4')
insta.login()
insta.findMyFollowers(5)

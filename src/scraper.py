from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

class Scraper():

    def __init__(self, log=False):
        self.log = log
        self.ser = Service(os.path.expanduser('~/Downloads/chromedriver_win32/chromedriver.exe'))
        self.opt = webdriver.ChromeOptions()
        self.opt.binary_location = os.path.expanduser('~/Downloads/chrome-win/chrome-win/chrome.exe')
        if self.log:
            self.opt.add_experimental_option("detach", True)  # do not terminate window when finished
        else:
            self.opt.add_argument('--headless=new')
            self.opt.add_experimental_option("excludeSwitches", ["enable-logging"])  # run in silent mode
        self.driver = webdriver.Chrome(service=self.ser, options=self.opt)
        self.website = 'http://audible.com/'

    def rate(self, keyword):
        self.driver.get(self.website)
        # searching
        search = self.driver.find_element(By.NAME, 'keywords')
        search.send_keys(keyword)
        search.submit()
        # selection
        select = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[5]/div/div[2]/div[4]/div/div/div/span/ul/li[1]/div/div[1]/div/div[2]/div/div/span/ul/li[1]/h3/a')
        select.click()
        # rating
        stars = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[8]/div[2]/div/div[3]/div/div/div/div[2]/span/ul/li[6]/span[2]').text
        stars = float(stars.replace(',', '.'))
        both = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[8]/div[2]/div/div[3]/div/div/div/div[2]/span/ul/li[6]').text.split('\n')[1]
        count = None    # ToDo: extract from 'both' or read from json
        self.driver.quit()
        return stars, both

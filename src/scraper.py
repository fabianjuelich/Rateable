from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

class Scraper():

    def __init__(self, log=False, directlink=False):
        self.log = log
        self.directlink = directlink
        self.ser = Service(os.path.abspath(os.path.join(os.path.dirname(__file__), '../assets/chromedriver_win32/chromedriver.exe')))
        self.opt = webdriver.ChromeOptions()
        self.opt.binary_location = os.path.abspath(os.path.join(os.path.dirname(__file__), '../assets/chrome-win/chrome.exe'))
        if self.log:
            self.opt.add_experimental_option("detach", True)  # do not terminate window when finished
        else:
            self.opt.add_argument('--headless=new')
            self.opt.add_experimental_option("excludeSwitches", ["enable-logging"])  # run in silent mode
        self.driver = webdriver.Chrome(service=self.ser, options=self.opt)
        if not directlink:
            self.website = 'https://audible.de/'

    def __scrape_rating(self, keywords:str):
        if not self.directlink:
            # searching
            self.driver.get(self.website)
            search = self.driver.find_element(By.NAME, 'keywords')
            search.send_keys(keywords)
            search.submit()
        else:
            self.website = f'https://audible.de/search?keywords={keywords.replace(" ", "+")}'
            self.driver.get(self.website)
        # selection
        select = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[5]/div/div[2]/div[4]/div/div/div/span/ul/li[1]/div/div[1]/div/div[2]/div/div/span/ul/li[1]/h3/a')
        select.click()
        # rating
        stars = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[8]/div[2]/div/div[3]/div/div/div/div[2]/span/ul/li[6]/span[2]').text
        text = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[8]/div[2]/div/div[3]/div/div/div/div[2]/span/ul/li[6]').text.split('\n')[1]
        searchResult = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[8]/div[2]/div/div[3]/div/div/div/div[2]/span/ul/li[1]/h1').text
        url = self.driver.find_element(By.XPATH, '/html/head/meta[11]').get_attribute('content')
        return stars, text, searchResult, url

    def __convert_rating(self, stars):
        # ToDo: consider edgecases 0 and 5
        max = 256
        per = stars/4
        bit = per*max-64
        return bit

    def __format_number(self, text):
        i = 1
        number = ''
        while text[i-1] != '(':
            i+=1
        while text[i] != ' ':
            number+=text[i]
            i+=1
        return int(number.replace('.', ''))

    def get_rating(self, keyword, byte=False):
        try:
            stars, text, searchResult, url = self.__scrape_rating(keyword)
            stars = float(stars.replace(',', '.'))
            return self.__convert_rating(stars) if byte else stars, self.__format_number(text), searchResult, url
        except:
            return 'NULL', 'NULL', 'N/A', 'N/A'

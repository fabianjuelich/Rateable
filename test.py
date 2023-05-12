from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import sys
import os
import eyed3
from mutagen.easyid3 import EasyID3

log = False

ser = Service(os.path.expanduser('~/Downloads/chromedriver_win32/chromedriver.exe'))
opt = webdriver.ChromeOptions()
opt.binary_location = os.path.expanduser('~/Downloads/chrome-win/chrome-win/chrome.exe')
if log:
    opt.add_experimental_option("detach", True)  # do not terminate window when finished
    pass
else:
    opt.add_argument('--headless=new')
    opt.add_experimental_option("excludeSwitches", ["enable-logging"])  # run in silent mode
driver = webdriver.Chrome(service=ser, options=opt)

website = 'http://audible.com/'
file = sys.argv[1]
keyword, _ = os.path.splitext(os.path.basename(file))

driver.get(website)
# searching
search = driver.find_element(By.NAME, 'keywords')
search.send_keys(keyword)
search.submit()
# selection
select = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[5]/div/div[2]/div[4]/div/div/div/span/ul/li[1]/div/div[1]/div/div[2]/div/div/span/ul/li[1]/h3/a')
select.click()
# rating
stars = driver.find_element(By.XPATH, '/html/body/div[1]/div[8]/div[2]/div/div[3]/div/div/div/div[2]/span/ul/li[6]/span[2]').text
stars = float(stars.replace(',', '.'))
both = driver.find_element(By.XPATH, '/html/body/div[1]/div[8]/div[2]/div/div[3]/div/div/div/div[2]/span/ul/li[6]').text.split('\n')[1]
count = None    # ToDo: extract from 'both' or read from json

driver.quit()

def convert_rating(stars):
    max = 256
    per = stars/4
    bit = per*max-64
    return bit

# writing
# eyed3
audiofile = eyed3.load(file)#, tag_version=(2,3,0))
if audiofile:
    # print(type(audiofile))
    # print(audiofile.tag.version)
    # print(audiofile.tag.title)
    audiofile.tag.popularities.set('-', convert_rating(stars), 0)
    audiofile.tag.comments.set(both)
    audiofile.tag.save(file)#, version=(2,3,0))
# # mutagen
# EasyID3.RegisterTextKey('rating', 'POPM')
# audiofile = EasyID3(file)
# print(audiofile)
# audiofile['rating'] = '3'
# audiofile.save()

print(both)
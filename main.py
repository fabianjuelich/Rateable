import sys
import os
from src.scraper import Scraper
# from src.id3 import ID3
from src.gui import App
from configparser import ConfigParser

def convert_rating(stars):
    max = 256
    per = stars/4
    bit = per*max-64
    return bit

gui = App()
# scraper = Scraper(False)
# id3 = ID3()

if len(sys.argv) > 1:
    file = sys.argv[1]
    keyword, _ = os.path.splitext(os.path.basename(file))
else:
    gui.mainloop()
    
# stars, both = scraper.rate(keyword)
# id3.modify([file], convert_rating(stars), both)

# print(both)
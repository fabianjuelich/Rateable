import sys
import os
from src.scraper import Scraper
# from src.id3 import ID3
from src.gui import App
from configparser import ConfigParser
from src.config import Config

conf = Config()
scraper = Scraper(log=False, directlink=False)
# id3 = ID3()
gui = App(conf, scraper)

if len(sys.argv) > 1:
    file = sys.argv[1]
    keyword, _ = os.path.splitext(os.path.basename(file))
else:
    gui.mainloop()
    
# id3.modify([file], convert_rating(stars), both)

print(scraper.get_rating(keyword))
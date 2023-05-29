import sys
from src.config import Config
from src.scraper import Scraper
from src.keywords import Keywords
# from src.id3 import ID3
from src.database import Database
from src.excel import Excel
from src.gui import App
import atexit

conf = Config()
scraper = Scraper(log=False, directlink=True)
keywords = Keywords()
# id3 = ID3()
database = Database(conf.get_db_path())
excel = Excel()
gui = App(conf, scraper, keywords, database, excel)

if len(sys.argv) > 1:
    path = sys.argv[1]
    for keyword in keywords.get(path):
        print(keyword, scraper.get_rating(keyword))
else:
    gui.mainloop()

def exit_handler():
    scraper.driver.quit()

atexit.register(exit_handler)

import customtkinter as ctk
from tkinter import filedialog
import os
import time

class App(ctk.CTk):

    def __init__(self, conf, scraper, keywords, database, excel):
        super().__init__()

        ctk.set_default_color_theme(os.path.join(os.path.dirname(__file__), '../assets/custom_theme.json'))
        self.title('ScrapeRate')
        self.geometry('400x200')

        for row in range(6):
            self.grid_rowconfigure(row, weight=1 if row in [0, 5] else 0)
        for col in range(4):
            self.grid_columnconfigure(col, weight=1)

        self.conf = conf
        self.scraper = scraper
        self.keywords = keywords
        self.database = database
        self.excel = excel

        # widgets
        self.label_info = ctk.CTkLabel(self, text='💽 Select audiobooks')
        self.button_folder = ctk.CTkButton(self, text='📂 Open Explorer', command=self.callback_folder)
        self.button_confirm = ctk.CTkButton(self, text='Confirm', command=self.callback_confirm, state='disabled')
        self.button_update = ctk.CTkButton(self, text='🔄 Update')  # ToDo: function for refreshing index
        # layout
        self.label_info.grid(row=1, column=1, columnspan=2, pady=(0, 10))
        self.button_folder.grid(row=2, column=1, columnspan=2, pady=(0, 5), sticky='we')
        self.button_confirm.grid(row=3, column=1, columnspan=2, pady=(5, 5), sticky='we')
        self.button_update.grid(row=4, column=1, columnspan=2, pady=(5, 0))
        # switch
        self.folder_switch = False
        self.confirm_switch = False

    def callback_folder(self):
        path = filedialog.askdirectory(title='💽 Select audiobooks', initialdir=os.path.expanduser('~/'))
        if path:
            self.buffer = False
            self.path = path
            self.confirm_switch = False
            self.button_confirm.configure(text='Confirm', text_color='#FFFFFF', state='disabled')
            self.button_folder.configure(text=os.path.basename(path), text_color=("#AAAAAA", "#777777"))
            self.button_confirm.configure(state='normal')
            self.folder_switch = True
            self.label_info.configure(text='✔ Audiobooks selected')

    def callback_confirm(self):
        if self.confirm_switch:
            os.startfile(self.conf.get_excel_path())
            self.label_info.configure(text='💽 Select audiobooks')
            self.button_confirm.configure(text='Confirm', text_color='#FFFFFF', state='disabled')
            self.confirm_switch = False
        elif not self.buffer:
            keywords = self.keywords.get(self.path)
            remaining = len(keywords)
            self.label_info.configure(text='⏳ Please wait')
            self.update_idletasks()
            for keyword in keywords:
                start = time.time()
                stars, number = self.scraper.get_rating(keyword)
                # ToDo: read and add metadata from file
                keywords[keyword]['stars'] = stars
                keywords[keyword]['number'] = number
                remaining-=1
                duration = remaining * (time.time()-start)
                if remaining:
                    self.label_info.configure(text=f'⌛ Please wait ({int(duration)} s left)')
                else:
                    self.label_info.configure(text='Specify save path')
                self.update_idletasks()
            self.database.insert(keywords)
            self.buffer = True
        if not self.conf.get_excel_path():
            self.conf.set_excel_path(filedialog.asksaveasfilename(initialdir=os.getcwd(), initialfile='ScrapeRate.xlsx'))
        if not self.confirm_switch:
            try:
                self.excel.create(self.database.table, self.database.connection, self.conf.get_excel_path())
                self.confirm_switch = True
                self.folder_switch = False
                self.button_folder.configure(text='📂 Open Explorer', text_color='#FFFFFF')
                self.label_info.configure(text=f'💾 Saved to {os.path.basename(self.conf.get_excel_path())}')
                self.button_confirm.configure(text='Open result', text_color=("#AAAAAA", "#777777"))
                self.buffer = False
            except Exception as e:
                print(e)
                self.label_info.configure(text='⚠️ Invalid path')

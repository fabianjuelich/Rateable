import customtkinter as ctk
from tkinter import filedialog
import os
from src.config import Config

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        ctk.set_default_color_theme('assets/custom_theme.json')

        self.title('ScrapeRate')
        self.geometry('400x200')

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.conf = Config()

        # widgets
        self.label_info = ctk.CTkLabel(self, text='Choose audiobook(s)')
        self.button_folder = ctk.CTkButton(self, text='Open Explorer', command=self.callback_folder)
        self.button_confirm = ctk.CTkButton(self, text='Confirm', command=self.callback_confirm, state='disabled')
        # layout
        self.label_info.grid(row=1, column=1, columnspan=2, pady=(0, 15))
        self.button_folder.grid(row=2, column=1, columnspan=2, pady=(0, 5), sticky='we')
        self.button_confirm.grid(row=3, column=1, columnspan=2, pady=5, sticky='we')
        # switch
        self.folder_switch = False
        self.confirm_switch = False

    def callback_folder(self):
        folder = filedialog.askdirectory(title='Choose audiobook(s)', initialdir=os.path.expanduser('~/'))
        if folder:
            self.folder = folder
            self.confirm_switch = False
            self.button_confirm.configure(text='Confirm', text_color='#FFFFFF', state='disabled')
            self.button_folder.configure(text=os.path.basename(folder), text_color=("#AAAAAA", "#777777"))
            self.button_confirm.configure(state='normal')
            self.folder_switch = True
            self.label_info.configure(text='Audiobook(s) selected')

    def callback_confirm(self):
        if self.confirm_switch:
            # ToDo: open excel file
            self.label_info.configure(text='Choose audiobook(s)')
            self.button_confirm.configure(text='Confirm', text_color='#FFFFFF', state='disabled')
            pass
        else:
            # ToDo: create list of audiobooks with with first filename
            # ToDo: read metadata from files
            # ToDo: scrape ratings for audiobooks
            # ToDo: save data to db
            if not self.conf.get_excel_path():
                self.conf.set_excel_path(filedialog.asksaveasfilename(initialdir=os.getcwd(), initialfile='ScrapeRate.xlsx'))
            try:
                with open(self.conf.get_excel_path(), 'w') as excel:
                    pass    # ToDo: write excel

                self.confirm_switch = True
                
                self.folder_switch = False
                self.button_folder.configure(text='Open Explorer', text_color='#FFFFFF')
                    
                self.label_info.configure(text=f'Saved to {os.path.basename(self.conf.get_excel_path())}')

                self.button_confirm.configure(text='Open result', text_color=("#AAAAAA", "#777777"))
            except:
                self.label_info.configure(text='Invalid path')

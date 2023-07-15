import customtkinter as ctk
from tkinter import filedialog
import os
import time
from enum import Enum, auto
from glob import glob

class Mode(Enum):
    INSERT = auto(),
    UPDATE = auto()

class App(ctk.CTk):

    def __init__(self, conf, scraper, keywords, id3, database, excel):
        super().__init__()

        ctk.set_default_color_theme(os.path.join(os.path.dirname(__file__), '../assets/custom_theme.json'))
        self.title('Rateable')
        self.geometry('400x240')
        self.iconbitmap(os.path.join(os.path.dirname(__file__), '../assets/Icons/icons8-fünf-von-fünf-sternen-64.ico'))

        for row in range(7):
            self.grid_rowconfigure(row, weight=1 if row in [0, 6] else 0)
        for col in range(4):
            self.grid_columnconfigure(col, weight=1)

        self.conf = conf
        self.scraper = scraper
        self.keywords = keywords
        self.id3 = id3
        self.database = database
        self.excel = excel
        self.insert_buffer = False
        self.update_buffer = False
        self.path = ''
        self.columns = self.database.get_column_names()
        self.data_keys = self.columns.copy()
        self.data_keys.remove('keyword')
        self.data_keys.remove('path')

        # variables
        self.variable_tag_type = ctk.StringVar(value='ID3')
        self.variable_id3_update = ctk.BooleanVar(value=False)
        # widgets
        self.label_info = ctk.CTkLabel(self, text='💽 Select audiobooks')
        self.button_folder = ctk.CTkButton(self, text='📂 Open Explorer', command=self.callback_folder)
        self.button_confirm = ctk.CTkButton(self, text='Confirm', command=self.callback_confirm, state=ctk.DISABLED)
        self.button_update = ctk.CTkButton(self, text='🔄 Update', command=self.callback_update)
        self.switch_tag_type = ctk.CTkSwitch(self, text='Use ID3 tags', command=self.callback_metadata, variable=self.variable_tag_type, offvalue='ID3', onvalue='Audible')
        self.checkbox_id3_update = ctk.CTkCheckBox(self, text='Update ID3 tags', variable=self.variable_id3_update, offvalue=False, onvalue=True, state=ctk.DISABLED)
        # layout
        self.label_info.grid(row=1, column=1, columnspan=2, pady=(0, 10))
        self.button_folder.grid(row=2, column=1, columnspan=2, pady=(0, 5), sticky='we')
        self.button_confirm.grid(row=3, column=1, columnspan=2, pady=(5, 5), sticky='we')
        self.button_update.grid(row=4, column=1, columnspan=2, pady=(5, 5))
        self.switch_tag_type.grid(row=5, column=1, columnspan=1, pady=(10, 0))
        self.checkbox_id3_update.grid(row=5, column=2, columnspan=1, pady=(5, 0))
        # states
        self.confirm_state = False

    def callback_folder(self):
        path = filedialog.askdirectory(title='💽 Select audiobooks', initialdir=self.path if self.path else os.path.expanduser('~/'))
        if path:
            self.buffer = False
            self.path = path
            self.confirm_state = False
            self.button_confirm.configure(text='Confirm', text_color=('#000000', '#FFFFFF'), state=ctk.NORMAL)
            self.button_folder.configure(text=os.path.basename(path), text_color=('#000000', '#FFFFFF'))
            self.label_info.configure(text='✅ Audiobooks selected')

    def callback_confirm(self):
        if self.confirm_state:
            os.startfile(self.conf.get_excel_path())
        elif not self.insert_buffer:
            keywords = self.keywords.get(self.path)
            if keywords:
                self.populate(Mode.INSERT, keywords)
            else:
                self.label_info.configure(text='⚠️ No audiobooks found')
        if self.insert_buffer:
            self.ask_excel_path()
            try:
                self.excel.create(self.database.table, self.database.connection, self.conf.get_excel_path())
                self.confirm_state = True
                self.label_info.configure(text=f'💾 Saved to {os.path.basename(self.conf.get_excel_path())}')
                self.button_confirm.configure(text='🗖 Open result', text_color=('#000000', '#FFFFFF'))
                self.insert_buffer = False
                self.update_buffer = False
            except Exception as e:
                print(e)
                self.label_info.configure(text='⚠️ Error creating excel file')

    def callback_update(self):
        if not self.update_buffer:
            data = {}
            keywords = [row[0] for row in self.database.select()]
            for keyword in keywords:
                data[keyword] = {}
            if data:
                self.populate(Mode.UPDATE, data)
            else:
                self.label_info.configure(text='⚠️ Table is empty')
        if self.update_buffer:
            self.ask_excel_path()
            try:
                self.excel.create(self.database.table, self.database.connection, self.conf.get_excel_path())
                self.button_confirm.configure(text='🗖 Open result', text_color=('#000000', '#FFFFFF'), state=ctk.NORMAL)
                self.label_info.configure(text='☁ Successfully updated')
                self.confirm_state = True
                self.update_buffer = False
            except Exception as e:
                print(e)
                self.label_info.configure(text='⚠️ Error creating excel file')

    def populate(self, mode, data):
        remaining = len(data)
        self.label_info.configure(text='⏳ Please wait')
        self.update_idletasks()
        duration = 0
        for keyword in data:
            start = time.time()
            data[keyword].update(self.scraper.get_rating(keyword, self.data_keys, tags=True if self.variable_tag_type.get() == 'Audible' else False))
            if self.variable_tag_type.get() == 'ID3':
                audiofiles = glob(f'{data[keyword]["path"]}/*.mp3')
                audiofile = audiofiles[0] if audiofiles else None
                data[keyword].update(dict(zip(self.data_keys[3:10], self.id3.read(audiofile, ['title', 'artist', 'author', 'length', 'date', 'comment', 'image']))))   # image missing and author/artist needs to be tested + calc duration over all audiofiles
            remaining-=1
            if data[keyword]['url'] != 'N/A':
                duration = remaining * (time.time()-start)
            if duration and remaining:
                if duration > 60:
                    min, sec = map(int, divmod(duration, 60))
                    left = f'{min}m {sec}s'
                elif duration > 3600:
                    hour, min = map(int, divmod(duration, 3600))
                    left = f'{hour}h {min}m'
                else:
                    left = f'{int(duration)}s'
                self.label_info.configure(text=f'⌛ Please wait ({left} left)')
            self.update_idletasks()
        match(mode):
            case Mode.INSERT:
                self.database.insert(data)
                self.update_buffer = False
                self.insert_buffer = True
            case Mode.UPDATE:
                self.database.update(data)
                self.insert_buffer = False
                self.update_buffer = True

    def ask_excel_path(self):
        if not os.path.isfile(self.conf.get_excel_path()):
            self.label_info.configure(text='📁 Specify save path')
            self.update_idletasks()
            self.conf.set_excel_path(filedialog.asksaveasfilename(
                initialdir=os.path.dirname(self.conf.get_excel_path()) if self.conf.get_excel_path() else os.getcwd(),
                initialfile='Rateable.xlsx',
                filetypes=[('Excel files', '.xlsx .xls')]
            ))

    def callback_metadata(self):
        match (self.variable_tag_type.get()):
            case 'Audible':
                self.switch_tag_type.configure(text='Use Audible tags')
                #self.checkbox_update_metadata.configure(state=ctk.NORMAL)
            case 'ID3':
                self.switch_tag_type.configure(text='Use ID3 tags')
                #self.checkbox_update_metadata.configure(state=ctk.DISABLED)
                #self.variable_metadata_update = False

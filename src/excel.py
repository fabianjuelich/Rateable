import pandas as pd
from win32com import client as win32
import openpyxl as op

class Excel():

    def create(self, table, con, path):
        df = pd.read_sql_query(f'SELECT * FROM {table}', con)
        df.columns = ['Name', 'Rating stars', 'Number of ratings', 'Audible', 'Title', 'Author', 'Read by', 'Duration', 'Published', 'Description', 'Image', 'Path']
        df.drop('Description', axis=1, inplace=True)
        df['Rating stars'] = df['Rating stars'].apply(self.__clean)
        df['Number of ratings'] = df['Number of ratings'].apply(self.__clean)
        df['Rating stars'] = df.apply(lambda row: self.__hyperlink(row['Audible'], row['Rating stars']), axis=1)
        df.drop('Audible', axis=1, inplace=True)
        df['Image'] = df['Image'].apply(self.__image)
        #df['Path'] = df['Path'].apply(self.hyperlink, args=('Explorer',))
        df['Path'] = df.apply(lambda row: self.__hyperlink(row['Path'], row['Name']), axis=1)
        df.drop('Name', axis=1, inplace=True)
        df = df.reindex(['Author', 'Title', 'Rating stars', 'Number of ratings', 'Read by', 'Duration', 'Published', 'Image', 'Path'], axis=1)
        df.to_excel(path, index=False)
        self.__auto_adjust_width(path)

    def __hyperlink(self, link, name):
        return f'=HYPERLINK("{link}", "{name}")' if link != 'N/A' else ''

    def __image(self, link, name='Image'):
        return f'=IMAGE("{link}", "{name}")' if link != 'N/A' else ''

    def __clean(self, cell):
        return cell if cell != 'NULL' else ''

    def __auto_adjust_width(self, path):
        xlsx = win32.gencache.EnsureDispatch('Excel.Application')
        xlsx.Visible = False
        wb = xlsx.Workbooks.Open(path)
        ws = wb.Worksheets('Sheet1')
        ws.Columns.AutoFit()
        wb.Save()
        xlsx.Application.Quit()

    def __center_horizontally(self, path):
        wb = op.load_workbook(path)
        ws = wb.worksheets[0]
        # whole column

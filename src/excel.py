import pandas as pd

class Excel():
    def create(self, table, con, path):
        df = pd.read_sql_query(f'SELECT * FROM {table}', con)
        df.columns = ['Name', 'Rating stars', 'Number of ratings', 'Audible', 'Title', 'Author', 'Read by', 'Duration', 'Published', 'Description', 'Image', 'Path']
        df.drop('Description', axis=1, inplace=True)
        df['Rating stars'] = df['Rating stars'].apply(self.clean)
        df['Number of ratings'] = df['Number of ratings'].apply(self.clean)
        df['Rating stars'] = df.apply(lambda row: self.hyperlink(row['Audible'], row['Rating stars']), axis=1)
        df.drop('Audible', axis=1, inplace=True)
        df['Image'] = df['Image'].apply(self.image)
        #df['Path'] = df['Path'].apply(self.hyperlink, args=('Explorer',))
        df['Path'] = df.apply(lambda row: self.hyperlink(row['Path'], row['Name']), axis=1)
        df.drop('Name', axis=1, inplace=True)
        df = df.reindex(['Author', 'Title', 'Rating stars', 'Number of ratings', 'Read by', 'Duration', 'Published', 'Image', 'Path'], axis=1)
        df.to_excel(path, index=False)

    def hyperlink(self, link, name):
        return f'=HYPERLINK("{link}", "{name}")' if link != 'N/A' else ''

    def image(self, link, name='Image'):
        return f'=IMAGE("{link}", "{name}")' if link != 'N/A' else ''

    def clean(self, cell):
        return cell if cell != 'NULL' else ''

import pandas as pd

class Excel():
    def create(self, table, con, path):
        df = df = pd.read_sql_query(f'SELECT * FROM {table}', con)
        df.columns = ['Name', 'Rating stars', 'Number of ratings', 'Source', 'Path']
        df['Source'] = df['Source'].apply(self.hyperlink, args=('Audible',))
        df['Path'] = df['Path'].apply(self.hyperlink, args=('Explorer',))
        df.to_excel(path, index=False)

    def hyperlink(self, link, name):
        return f'=HYPERLINK("{link}", "{name}")' if link != 'N/A' else ''

import pandas as pd

class Excel():
    def create(self, table, con, path):
        df = df = pd.read_sql_query(f'SELECT * FROM {table}', con)
        df.columns = ['Name', 'Rating stars', 'Number of ratings', 'Path to audiobook']
        df.to_excel(path, index=False)

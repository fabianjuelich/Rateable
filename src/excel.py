import pandas as pd

class Excel():
    def create(self, table, con, path):
        df = df = pd.read_sql_query(f'SELECT * FROM {table}', con)
        df.to_excel(path)

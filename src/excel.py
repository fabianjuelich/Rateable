import pandas as pd

class Excel():
    def create(self, table, con, path):
        df = pd.read_sql_query(f'SELECT * FROM {table}', con)
        df.columns = ['Name', 'Rating stars', 'Number of ratings', 'Search Result', 'Audible', 'Path']
        df['Rating stars'] = df['Rating stars'].apply(self.clean)
        df['Number of ratings'] = df['Number of ratings'].apply(self.clean)
        df['Audible'] = df.apply(lambda row: self.hyperlink(row['Audible'], row['Search Result']), axis=1)
        df.drop('Search Result', axis=1, inplace=True)
        df['Path'] = df['Path'].apply(self.hyperlink, args=('Explorer',))
        df.to_excel(path, index=False)

    def hyperlink(self, link, name):
        return f'=HYPERLINK("{link}", "{name}")' if link != 'N/A' else ''

    def clean(self, cell):
        return cell if cell != 'NULL' else ''

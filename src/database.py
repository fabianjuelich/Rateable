import sqlite3

class Database:
    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
        self.table = 'Audiobooks'

        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {self.table} (
                keyword TEXT PRIMARY KEY,
                stars REAL,
                number INTEGER,
                url TEXT,
                path TEXT
            )
            ''')

    def select(self):
        return self.cursor.execute(f'SELECT * FROM {self.table}').fetchall()

    def insert(self, rows):
        for key, value in rows.items():
            self.cursor.execute(f'''
                INSERT OR REPLACE INTO {self.table} VALUES (
                    ?,
                    ?,
                    ?,
                    ?,
                    ?
                )
            ''', (
                    key,
                    value['stars'],
                    value['number'],
                    value['url'],
                    value['path']
                )
            )
        self.connection.commit()

    def update(self, rows):
        for key, value in rows.items():
            self.cursor.execute(f'''
                UPDATE {self.table} SET
                    stars = {value['stars']},
                    number = {value['number']},
                    url = '{value['url']}'
                WHERE
                    keyword = '{key}'
            ''')
        self.connection.commit()

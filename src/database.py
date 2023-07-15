import sqlite3
import os

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
                title TEXT,
                author TEXT,
                speaker TEXT,
                length TEXT,
                date TEXT,
                description TEXT,
                image TEXT,
                path TEXT
            )
            ''')

    def select(self):
        return self.cursor.execute(f'SELECT * FROM {self.table}').fetchall()

    def insert(self, rows):
        for key, value in rows.items():
            self.cursor.execute(
                f'INSERT OR REPLACE INTO {self.table} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (
                    key,
                    *[value[key] for key in [column for column in self.get_column_names() if column != 'keyword']]
                )   
            )
        self.connection.commit()

    def update(self, rows):
        for key, value in rows.items():
            self.cursor.execute(f'''
                UPDATE {self.table} SET
                    stars = ?,
                    number = ?,
                    url = ?,
                    title = ?,
                    author = ?,
                    speaker = ?,
                    length = ?,
                    date = ?,
                    description = ?,
                    image = ?,
                    path = {'path' if os.path.exists(self.cursor.execute(f'SELECT path FROM {self.table} WHERE keyword = ?', (key,)).fetchone()[0]) else '"N/A"'}
                WHERE
                    keyword = ?
                ''', (
                    *[value[key] for key in [column for column in self.get_column_names() if column not in ['keyword', 'path']]],
                    key
                )
            )
        self.connection.commit()

    def get_column_names(self):
        return [name[0] for name in self.cursor.execute(f'SELECT name FROM pragma_table_info("{self.table}")').fetchall()]

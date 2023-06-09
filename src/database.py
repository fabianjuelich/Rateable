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
            self.cursor.execute(f'''
                INSERT OR REPLACE INTO {self.table} VALUES (
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
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
                    value['title'],
                    value['author'],
                    value['speaker'],
                    value['length'],
                    value['date'],
                    value['description'],
                    value['image'],
                    value['path']
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
                    value['stars'],
                    value['number'],
                    value['url'],
                    value['title'],
                    value['author'],
                    value['speaker'],
                    value['length'],
                    value['date'],
                    value['description'],
                    value['image'],
                    key
                )
            )
        self.connection.commit()

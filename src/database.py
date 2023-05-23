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
                path TEXT
            )
            ''')

    def insert(self, rows):
        for key, value in rows.items():
            self.cursor.execute(f'''
                INSERT OR REPLACE INTO {self.table} VALUES (
                    ?, ?, ?, ?
                );
                ''', (
                    key,
                    value['stars'],
                    value['number'],
                    value['path']
                ))
        self.connection.commit()


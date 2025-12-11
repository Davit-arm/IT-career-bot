import sqlite3
import json
class DB_manager():

    def __init__(self, db_name):
        self.db_name = db_name

    def make_tables(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    answers TEXT NOT NULL,
                    ai_summary TEXT NOT NULL,
                    date TEXT)
''')
        con.commit()
        con.close()

    def add_info(self, user_id, answers, ai_summary, date):
        try:
            con = sqlite3.connect(self.db_name)
            cur = con.cursor()
            cur.execute('''INSERT INTO users (user_id, answers, ai_summary, date) VALUES (?, ?, ?, ?)''',(user_id, answers, ai_summary, date))
            con.commit()
            con.close()
            return 'Info added successfully'
        except Exception as e:
            return f'Error adding info: {e}'

    def get_all_info(self):
        try:
            con = sqlite3.connect(self.db_name)
            cur = con.cursor()
            cur.execute('''SELECT * FROM users''')
            rows = cur.fetchall()
            return rows
        except Exception as e:
            return f'Error fetching info: {e}'

#test = DB_manager('test.db')
#print(test.get_all_info())
# test.make_tables()
# answers = {'q1': 'Answer1', 'q2': 'Answer2', 'q3': 'Answer3'}
# answers_str = str(answers)
# print(test.add_info(54321, answers_str, 'AI summary example', '2024-05-01'))
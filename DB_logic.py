import sqlite3
class DB_manager():

    def __init__(self, db_name):
        self.db_name = db_name

    def make_tables(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS users_quiz (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    answers TEXT NOT NULL,
                    ai_summary TEXT NOT NULL,
                    feedback TEXT,
                    feedback_description TEXT,
                    date TEXT)
''')
        cur.execute('''CREATE TABLE IF NOT EXISTS users_describe (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    description TEXT NOT NULL,
                    ai_summary TEXT NOT NULL,
                    feedback TEXT,
                    feedback_description TEXT,
                    date TEXT)
                     ''')
        con.commit()
        con.close()

    def add_info_quiz(self, user_id, answers, ai_summary, date):
        try:
            con = sqlite3.connect(self.db_name)
            cur = con.cursor()
            cur.execute('''INSERT INTO users_quiz (user_id, answers, ai_summary, date) VALUES (?, ?, ?, ?)''',(user_id, answers, ai_summary, date))
            con.commit()
            con.close()
            return 'Info added successfully'
        except Exception as e:
            return f'Error adding info: {e}'

    def get_all_info_quiz(self):
        try:
            con = sqlite3.connect(self.db_name)
            cur = con.cursor()
            cur.execute('''SELECT * FROM users_quiz''')
            rows = cur.fetchall()
            return rows
        except Exception as e:
            return f'Error fetching info: {e}'
        
    def add_feedback_quiz(self,ai_summary,feedback,feedback_description=None):
        try:
            con = sqlite3.connect(self.db_name)
            cur = con.cursor()
            cur.execute('''UPDATE users_quiz SET feedback = ?, feedback_description = ? WHERE ai_summary = ?''',(feedback,feedback_description,ai_summary))
            con.commit()
            con.close()
            return 'Feedback added successfully'
        except Exception as e:
            return f'Error adding feedback:{e}'
        
    def add_info_desc(self, user_id, description, ai_summary, date):
        try:
            con = sqlite3.connect(self.db_name)
            cur = con.cursor()
            cur.execute('''INSERT INTO users_describe (user_id, description, ai_summary, date) VALUES (?, ?, ?, ?)''',(user_id, description, ai_summary, date))
            con.commit()
            con.close()
            return 'Info added successfully'
        except Exception as e:
            return f'Error adding info: {e}'

    def get_all_info_desc(self):
        try:
            con = sqlite3.connect(self.db_name)
            cur = con.cursor()
            cur.execute('''SELECT * FROM users_describe''')
            rows = cur.fetchall()
            return rows
        except Exception as e:
            return f'Error fetching info: {e}'
        
    def add_feedback_desc(self,ai_summary,feedback,feedback_description=None):
        try:
            con = sqlite3.connect(self.db_name)
            cur = con.cursor()
            cur.execute('''UPDATE users_describe SET feedback = ?, feedback_description = ? WHERE ai_summary = ?''',(feedback,feedback_description,ai_summary))
            con.commit()
            con.close()
            return 'Feedback added successfully'
        except Exception as e:
            return f'Error adding feedback:{e}'

#test = DB_manager('test.db')
#print(test.get_all_info())
# test.make_tables()
# answers = {'q1': 'Answer1', 'q2': 'Answer2', 'q3': 'Answer3'}
# answers_str = str(answers)
# print(test.add_info(54321, answers_str, 'AI summary example', '2024-05-01'))
import os
import sqlite3
from datetime import datetime, timedelta


class StudyDatabase:
    def __init__(self, db_name="study_tracker.db"):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(current_dir, "..", db_name)
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS study_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                user_name TEXT,
                subject TEXT,
                start_time TEXT,
                end_time TEXT,
                duration_seconds INTEGER
            )
        """)

        try:
            cursor.execute("ALTER TABLE study_sessions ADD COLUMN user_name TEXT")
        except sqlite3.OperationalError:
            pass

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_subjects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                subject_name TEXT,
                UNIQUE(user_id, subject_name)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_goals (
                user_id INTEGER PRIMARY KEY,
                daily_hours INTEGER
            )
        """)

        # Жаңа кесте: Бір күндік план (Schedule) сақтау үшін
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_schedules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                time_slot TEXT,
                task_desc TEXT
            )
        """)

        conn.commit()
        conn.close()

    def add_custom_subject(self, user_id, subject_name):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO user_subjects (user_id, subject_name) VALUES (?, ?)", (user_id, subject_name))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()

    def get_user_subjects(self, user_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT subject_name FROM user_subjects WHERE user_id = ?", (user_id,))
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows] if rows else ["English", "Coding", "Math"]

    def set_daily_goal(self, user_id, hours):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO user_goals (user_id, daily_hours) VALUES (?, ?)", (user_id, hours))
        conn.commit()
        conn.close()

    def save_session(self, user_id, user_name, subject, start_time, end_time, duration):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO study_sessions (user_id, user_name, subject, start_time, end_time, duration_seconds)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (user_id, user_name, subject, start_time, end_time, duration))
        conn.commit()
        conn.close()

    def get_stats_data(self, user_id, today_str):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT subject, SUM(duration_seconds) FROM study_sessions WHERE user_id = ? GROUP BY subject",
                       (user_id,))
        rows = cursor.fetchall()

        cursor.execute("SELECT daily_hours FROM user_goals WHERE user_id = ?", (user_id,))
        goal_row = cursor.fetchone()
        daily_goal_hours = goal_row[0] if goal_row else 0

        cursor.execute("SELECT SUM(duration_seconds) FROM study_sessions WHERE user_id = ? AND start_time LIKE ?",
                       (user_id, f"{today_str}%"))
        today_row = cursor.fetchone()
        today_seconds = today_row[0] if today_row[0] else 0
        conn.close()

        return rows, daily_goal_hours, today_seconds

    def get_weekly_data(self, user_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        weekly_data = {}
        now = datetime.now()
        for i in range(6, -1, -1):
            day = now - timedelta(days=i)
            day_str = day.strftime("%Y-%m-%d")
            weekly_data[day_str] = 0
        cursor.execute("""
            SELECT date(start_time), SUM(duration_seconds) 
            FROM study_sessions 
            WHERE user_id = ? AND start_time >= date('now', '-7 days')
            GROUP BY date(start_time)
        """, (user_id,))
        for row in cursor.fetchall():
            if row[0] in weekly_data:
                weekly_data[row[0]] = round(row[1] / 3600, 1)
        conn.close()
        return weekly_data

    def get_leaderboard(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT user_name, SUM(duration_seconds), user_id 
            FROM study_sessions 
            GROUP BY user_id 
            ORDER BY SUM(duration_seconds) DESC 
            LIMIT 5
        """)
        rows = cursor.fetchall()
        conn.close()
        return rows

    # --- NEW SCHEDULE FUNCTIONS ---
    def add_schedule_task(self, user_id, time_slot, task_desc):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user_schedules (user_id, time_slot, task_desc) VALUES (?, ?, ?)",
                       (user_id, time_slot, task_desc))
        conn.commit()
        conn.close()

    def get_user_schedule(self, user_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT time_slot, task_desc FROM user_schedules WHERE user_id = ?", (user_id,))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def clear_user_schedule(self, user_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM user_schedules WHERE user_id = ?", (user_id,))
        conn.commit()
        conn.close()
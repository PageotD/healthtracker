import sqlite3
import uuid
from datetime import datetime, timedelta
from . import DBPATH

def create_user(user_name: str) -> None:
    conn = sqlite3.connect(DBPATH)
    cursor = conn.cursor()
    user_id = str(uuid.uuid4())
    cursor.execute("INSERT INTO user (user_id, user_name) VALUES (?, ?)", (user_id, user_name))
    conn.commit()
    conn.close()

def get_user_id(user_name: str) -> str|None:
    conn = sqlite3.connect(DBPATH)
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM user WHERE user_name = ?", (user_name,))
    user_id = cursor.fetchone()
    conn.close()
    return user_id

def retrieve_weight_data(user_id: str) -> list:
    conn = sqlite3.connect(DBPATH)
    cursor = conn.cursor()
    start_date = datetime.now() - timedelta(days=90)
    cursor.execute("SELECT measurement_datetime, weight_value FROM weight WHERE user_id = ? AND measurement_datetime >= ?", (user_id, start_date))
    weight_data = cursor.fetchall()
    conn.close()
    return weight_data
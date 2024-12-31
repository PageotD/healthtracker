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

def add_weight_data(user_id: str, datetime: str, weight_value: float) -> None:
    conn = sqlite3.connect(DBPATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO weight (user_id, measurement_datetime, weight_value) VALUES (?, ?, ?)", (user_id, datetime, weight_value))
    conn.commit()
    conn.close()

def retrieve_weight_data(user_id: str) -> list:
    conn = sqlite3.connect(DBPATH)
    cursor = conn.cursor()

    # Début et fin de la plage de dates
    start_date = datetime.now() - timedelta(days=30)
    end_date = datetime.now()

    # Générer une liste de toutes les dates dans l'intervalle
    date_range = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

    # Récupérer les données de poids depuis la BDD
    cursor.execute(
        "SELECT measurement_datetime, weight_value FROM weight WHERE user_id = ? AND measurement_datetime >= ?",
        (user_id, start_date)
    )
    weight_data = cursor.fetchall()
    conn.close()

    # Transformer les résultats de la BDD en un dictionnaire pour un accès rapide
    weight_dict = {datetime.strptime(row[0], "%Y-%m-%d").date(): row[1] for row in weight_data}

    # Construire la liste finale avec toutes les dates, même celles absentes
    chart_data = {
        "date": [],
        "weight": []
    }
    for date in date_range:
        date_only = date.date()
        chart_data["date"].append(date_only.strftime("%Y-%m-%d"))
        chart_data["weight"].append(weight_dict.get(date_only, None))

    return chart_data

def add_calories_data(user_id: str, datetime: str, calories_value: float) -> None:
    conn = sqlite3.connect(DBPATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO calories (user_id, measurement_datetime, calories_value) VALUES (?, ?, ?)", (user_id, datetime, calories_value))
    conn.commit()
    conn.close()

def retrieve_calories_data(user_id: str) -> list:
    conn = sqlite3.connect(DBPATH)
    cursor = conn.cursor()

    # Début et fin de la plage de dates
    start_date = datetime.now() - timedelta(days=30)
    end_date = datetime.now()

    # Générer une liste de toutes les dates dans l'intervalle
    date_range = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

    # Récupérer les données de poids depuis la BDD
    cursor.execute(
        "SELECT measurement_datetime, calories_value FROM calories WHERE user_id = ? AND measurement_datetime >= ?",
        (user_id, start_date)
    )
    calories_data = cursor.fetchall()
    conn.close()

    # Transformer les résultats de la BDD en un dictionnaire pour un accès rapide
    calories_dict = {datetime.strptime(row[0], "%Y-%m-%d").date(): row[1] for row in calories_data}

    # Construire la liste finale avec toutes les dates, même celles absentes
    chart_data = {
        "date": [],
        "calories": []
    }
    for date in date_range:
        date_only = date.date()
        chart_data["date"].append(date_only.strftime("%Y-%m-%d"))
        chart_data["calories"].append(calories_dict.get(date_only, None))

    return chart_data

def add_sleep_data(user_id: str, start_datetime: str, end_datetime: str) -> None:
    conn = sqlite3.connect(DBPATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sleep (user_id, start_datetime, end_datetime) VALUES (?, ?, ?)", (user_id, start_datetime, end_datetime))
    conn.commit()
    conn.close()

def retrieve_sleep_data(user_id: str) -> dict:
    conn = sqlite3.connect(DBPATH)
    cursor = conn.cursor()

    # Define the start and end date range
    start_date = datetime.now() - timedelta(days=30)
    end_date = datetime.now()

    # Generate a list of all dates in the range
    date_range = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

    # Query to retrieve sleep data from the database
    cursor.execute(
        "SELECT start_datetime, end_datetime FROM sleep WHERE user_id = ? AND start_datetime >= ?",
        (user_id, start_date)
    )
    sleep_data = cursor.fetchall()
    conn.close()

    # Process the sleep data and calculate durations in hours
    duration_dict = {}
    for row in sleep_data:
        # Parse ISO 8601 format
        start_dt = datetime.fromisoformat(row[0])
        end_dt = datetime.fromisoformat(row[1])
        duration = (end_dt - start_dt).total_seconds() / 3600  # Convert duration to hours
        duration_dict[start_dt.date()] = duration

    # Prepare the final chart data
    chart_data = {
        "date": [],
        "duration": []
    }
    for date in date_range:
        date_only = date.date()
        chart_data["date"].append(date_only.strftime("%Y-%m-%d"))
        chart_data["duration"].append(duration_dict.get(date_only, None))

    return chart_data

def add_activity_data(user_id: str, start_datetime: str, end_datetime: str) -> None:
    conn = sqlite3.connect(DBPATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO activity (user_id, start_datetime, end_datetime) VALUES (?, ?, ?)", (user_id, start_datetime, end_datetime))
    conn.commit()
    conn.close()

def retrieve_activity_data(user_id: str) -> dict:
    conn = sqlite3.connect(DBPATH)
    cursor = conn.cursor()

    # Define the start and end date range
    start_date = datetime.now() - timedelta(days=30)
    end_date = datetime.now()

    # Generate a list of all dates in the range
    date_range = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

    # Query to retrieve activity data from the database
    cursor.execute(
        "SELECT start_datetime, end_datetime FROM activity WHERE user_id = ? AND start_datetime >= ?",
        (user_id, start_date)
    )
    activity_data = cursor.fetchall()
    conn.close()

    # Process the sleep data and calculate durations in hours
    duration_dict = {}
    for row in activity_data:
        # Parse ISO 8601 format
        start_dt = datetime.fromisoformat(row[0])
        end_dt = datetime.fromisoformat(row[1])
        duration = (end_dt - start_dt).total_seconds() / 3600  # Convert duration to hours
        duration_dict[start_dt.date()] = duration

    # Prepare the final chart data
    chart_data = {
        "date": [],
        "duration": []
    }
    for date in date_range:
        date_only = date.date()
        chart_data["date"].append(date_only.strftime("%Y-%m-%d"))
        chart_data["duration"].append(duration_dict.get(date_only, None))

    return chart_data
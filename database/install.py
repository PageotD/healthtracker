import sqlite3
import sys
def create_database(schema_file: str, db_file: str):
    """
    Create a database from the given schema file.

    Args:
        schema_file (str): Path to the SQL schema file.
        db_file (str): Path to the SQLite database file to create.
    """
    try:
        # Connect to SQLite database
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        # Enable foreign keys in SQLite
        cursor.execute("PRAGMA foreign_keys = ON;")

        # Read the schema from the file
        with open(schema_file, 'r') as file:
            schema = file.read()

        # Execute the schema
        cursor.executescript(schema)
        connection.commit()
        print(f"Database created successfully at '{db_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            connection.close()

# Define paths for schema and database
schema_path = "schema.sql"  # Replace with the path to your schema file
database_path = "../healthtracker.db"    # Replace with your desired database file path

# Create the database
create_database(schema_path, database_path)

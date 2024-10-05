import mysql.connector
from mysql.connector import Error
import datetime

def connect_db():
    db_name = "fitness_center"
    user = "root"
    password = "[insert you passord]"
    host = "localhost"

    try:
        conn=mysql.connector.connect(
            database = db_name,
            user=user,
            password=password,
            host=host
        )

        if conn.is_connected():
            print ("Connected to MySQL database successfully")
            return conn
    except Error as e:
        print(f"Error: {e}")

def construct_tables():
    conn = connect_db()
    if conn is not None:
        try:
            cursor=conn.cursor()
            query =   """
                CREATE TABLE Members (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                age INT NULL
                );
                CREATE TABLE WorkoutSessions (
                session_id INT AUTO_INCREMENT PRIMARY KEY,
                member_id INT NOT NULL,
                date DATETIME NOT NULL,
                duration_minutes VARCHAR(25) NOT NULL,
                calories_burned VARCHAR(25) NOT NULL,
                FOREIGN KEY (member_id) REFERENCES Members(id)
                )
                """
            cursor.execute(query)
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
                print("MySQL connection is closed.")

def retrieve_data_members():
    conn = connect_db()
    if conn is not None:
        try:
            cursor=conn.cursor()
    
            query = "SELECT * FROM Members"
            
            cursor.execute(query)
            
            for row in cursor.fetchall():
                member_id,name,age = row
                print (f"Member ID: {member_id}, Name: {name}, Age: {age}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
                print("MySQL connection is closed.")

def retrieve_data_workout_sessions():
    conn = connect_db()
    if conn is not None:
        try:
            cursor=conn.cursor()
    
            query = "SELECT * FROM WorkoutSessions"
            
            cursor.execute(query)
            
            for row in cursor.fetchall():
                session_id,member_id,date,duration_minutes,calories_burned = row
                print(f"Session ID: {session_id}, Member ID: {member_id}, Session Date: {date.strftime("%Y-%m-%d")}, Duration (Minutes): {duration_minutes}, Calories Burned: {calories_burned}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
                print("MySQL connection is closed.")
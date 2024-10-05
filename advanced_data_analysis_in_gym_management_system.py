# Objective: The goal of this assignment is to advance your SQL querying skills within Python, focusing on specific SQL functions and clauses like BETWEEN. You will be working with the same gym database as in the previous assignment, comprising the Members and WorkoutSessions tables.

# Problem Statement: As a part of the gym's management team, you need to conduct an in-depth analysis of the membership data. Your task is to develop Python functions that execute advanced SQL queries for distinct department identification, employee count in each department, and age-based employee filtering.

# Task 1: SQL BETWEEN Usage

# Problem Statement: Retrieve the details of members whose ages fall between 25 and 30.
# Expected Outcome: A list of members (including their names, ages, etc) who are between the ages of 25 and 30.

from connect_mysql import connect_db

def get_members_in_age_range(start_age, end_age):
    conn = connect_db()
    if conn is not None:
        try:
            cursor=conn.cursor()
    
            query = "SELECT * FROM Members WHERE age BETWEEN %s AND %s "
            
            cursor.execute(query,(start_age,end_age))
            
            for row in cursor.fetchall():
                member_id,name,age = row
                print (f"Member ID: {member_id}, Name: {name}, Age: {age}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
                print("MySQL connection is closed.")
    # SQL query using BETWEEN
    # Execute and fetch results
import connect_mysql
import ErrorHandling

# 1. Gym Database Management with Python and SQL
# Objective: The aim of this assignment is to reinforce your understanding of Python's interaction with SQL databases, focusing on CRUD (Create, Read, Update, Delete) operations in the context of a gym's membership and workout session management system. You will work with two tables: 'Members' and 'WorkoutSessions'.

# Problem Statement: You are tasked with developing a Python application to manage a gym's database. The database consists of 'Members' and 'WorkoutSessions' tables. Your role is to implement various functions to add, retrieve, update, and delete records in these tables, ensuring data integrity and efficient data handling.

# Task 1: Add a Member

# Write a Python function to add a new member to the 'Members' table in the gym's database.

def add_member(name, age):
    conn = connect_mysql.connect_db()
    try:    
        if conn is not None:
            cursor=conn.cursor()
            new_member = (name, age)
            name_check_query = "SELECT * FROM members WHERE name = %s AND age = %s"
            cursor.execute(name_check_query,new_member)
            name_check_result = cursor.fetchall()
            if name_check_result == []:
                query = "INSERT INTO members (name,age) VALUES (%s,%s)"
                cursor.execute(query,new_member)
                conn.commit()
                print("New member added successfully!")
            else:
                raise ErrorHandling.MemberExists
    except ErrorHandling.MemberExists:
        ErrorHandling.MemberExists.handle_member_exists()
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed.")
    # SQL query to add a new member
    # Error handling for duplicate IDs or other constraints

# Expected Outcome: A Python function that successfully adds a new member to the 'Members' table in the gym's database. The function should handle errors gracefully, such as duplicate member IDs or violations of other constraints.


# Task 2: Add a Workout Session

# Develop a Python function to add a new workout session to the 'WorkoutSessions' table for a specific member.

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    conn = connect_mysql.connect_db()
    try:    
        if conn is not None:
            cursor=conn.cursor()
            id_check_query = "SELECT * FROM members WHERE id = %s"
            cursor.execute(id_check_query,(member_id, ))
            id_check_result = cursor.fetchall()
            if id_check_result == []:
                raise ErrorHandling.NoMemberFound
            else:
                query = "INSERT INTO workoutsessions (member_id,date,duration_minutes,calories_burned) VALUES (%s,%s,%s,%s)"
                cursor.execute(query,(member_id,date,duration_minutes,calories_burned))
                conn.commit()
                print("Workout Session Successfully added!")
    except ErrorHandling.NoMemberFound:
        ErrorHandling.NoMemberFound.handle_no_member_found()
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed.")

    # SQL query to add a new workout session
    # Error handling for invalid member ID or other constraints

# Expected Outcome: A Python function that adds a new workout session to the 'WorkoutSessions' table in the gym's database for a specific member. The function should handle errors gracefully, such as invalid member IDs or violations of other constraints.


# Task 3: Updating Member Information

# Implement a function to update the age of a member. Ensure that your function checks if the member exists before attempting the update.

def update_member_age(member_id, new_age):
    conn = connect_mysql.connect_db()
    try:    
        if conn is not None:
            cursor=conn.cursor()
            id_check_query = "SELECT * FROM members WHERE id = %s"
            cursor.execute(id_check_query,(member_id, ))
            id_check_result = cursor.fetchall()
            if id_check_result == []:
                raise ErrorHandling.NoMemberFound
            else:               
                updated_customer = (new_age, member_id)
                query = "UPDATE members SET age = %s WHERE id =  %s"
                cursor.execute(query,updated_customer)
                conn.commit()
                print("Memeber age successfully Updated!")
    except ErrorHandling.NoMemberFound:
        ErrorHandling.NoMemberFound.handle_no_member_found()
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed.")

    # SQL query to update age
    # Check if member exists
    # Error handling

# Expected Outcome: A Python function that updates the age of a member and handles cases where the member does not exist.


# Task 4: Delete a Workout Session

# Create a Python function to delete a workout session based on its session ID. Include error handling for cases where the session ID does not exist.

def delete_workout_session(session_id):
    conn = connect_mysql.connect_db()
    try:    
        if conn is not None:
            cursor=conn.cursor()
            id_check_query = "SELECT * FROM workoutsessions WHERE session_id = %s"
            cursor.execute(id_check_query,(session_id, ))
            id_check_result = cursor.fetchall()
            if id_check_result == []:
                raise ErrorHandling.NoSessionFound
            else:               
                query = "DELETE FROM workoutsessions WHERE session_id =  %s"
                cursor.execute(query,(session_id, ))
                conn.commit()
                print("Workout Session Successfully deleted!")
    except ErrorHandling.NoSessionFound:
        ErrorHandling.NoSessionFound.handle_no_session_found()
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed.")

    #SQL query to delete a session
    #Error handling for non-existent session ID

# Expected Outcome: A Python function that can delete a workout session using its session ID, with proper error handling for invalid IDs.
import connect_mysql
import gym_database_management_with_python_and_SQL as gdbm
from advanced_data_analysis_in_gym_management_system import get_members_in_age_range as gma

connect_mysql.construct_tables()

gdbm.add_member("John Doe",27)
gdbm.add_member("Jane Doe",30)
gdbm.add_member("H.N. Gibson",35)
gdbm.add_member("Maggie Gibson",31)

connect_mysql.retrieve_data_members()

gdbm.add_workout_session(1,"2024-01-01",30,150)
gdbm.add_workout_session(2,"2024-01-01",45,225)
gdbm.add_workout_session(3,"2024-01-01",50,250)
gdbm.add_workout_session(4,"2024-01-01",60,275)

connect_mysql.retrieve_data_workout_sessions()

gdbm.update_member_age(2,28)

connect_mysql.retrieve_data_members()

gdbm.delete_workout_session(3)

connect_mysql.retrieve_data_workout_sessions()

gma(25,30)
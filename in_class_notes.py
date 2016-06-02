# migration.py scaffold

import psycopg2

connection = psycopg2.connect("dbname=learning_sql user=dbperson")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS person_data;")

table_create_command = """CREATE TABLE person_data (
  full_name varchar(30),
  best_friend varchar(30),
  age numeric(3),
  birth_year numeric(4)
);"""

cursor.execute(table_create_command)

name = "Joel Taddei"
bestie = "Audrey"
age = 32
year = 1983
# do not use .format!!!!!!!!

cursor.execute("INSERT INTO person_data VALUES (%s, %s, %s, %s);", (name, bestie, age, year))

connection.commit()

cursor.close()
connection.close()
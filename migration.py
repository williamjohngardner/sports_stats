import psycopg2

connection = psycopg2.connect("dbname=learning_sql user=dbperson")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS orioles_stats;")

table_create_command = """CREATE TABLE orioles_stats (
  name varchar(30),
  position varchar(30),
  games numeric(3),
  at_bats numeric(3),
  runs numeric(3),
  hits numeric(4),
  doubles numeric(2),
  triples numeric(2),
  home_runs numeric(3),
  rbi numeric(3),
  strike_outs numeric(3),
  average numeric (4),
);"""

cursor.execute(table_create_command)

name
position
games
at_bats
runs
hits
doubles
triples
home_runs
rbi
strike_outs
average

cursor.execute("INSERT INTO person_data VALUES (%s, %s, %s, %s);", (name, bestie, age, year))

connection.commit()

cursor.close()
connection.close()
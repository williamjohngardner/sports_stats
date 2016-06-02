import psycopg2

connection = psycopg2.connect("dbname=orioles_stats user=billgardner")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS batting_avg;")

table_create = """CREATE TABLE batting_avg (
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
  average decimal (4)
);"""

cursor.execute(table_create)

# for row in results:
#     name = row[0]
#     position = row[1]
#     games = row[2]
#     at_bats = row[3]
#     runs = row[4]
#     hits = row[5]
#     doubles = row[6]
#     triples = row[7]
#     home_runs = row[8]
#     rbi = row[9]
#     strike_outs = row[10]
#     average = row[11]

# cursor.execute("INSERT INTO person_data VALUES (%s, %s, %s, %s);", (name, position, games, at_bats, runs, hits, doubles,
#                                                                     triples, home_runs, rbi, strike_outs, average))


cursor.execute("insert into batting_avg values"
               "('Kim','LF',19,55,8,21,4,0,1,3,8,0.382),"
               "('Machado','3B',51,207,38,65,21,0,13,31,40,0.314),"
               "('Reimold','LF',34,80,13,24,4,1,4,10,22,0.3),"
               "('Trumbo','RF',51,201,29,57,8,1,15,39,59,0.284),"
               "('Wieters','C',35,128,11,36,7,0,4,20,35,0.281),"
               "('Schoop','2B',51,187,20,50,10,1,8,30,44,0.267),"
               "('Rickard','LF',50,177,23,44,7,0,4,11,40,0.249),"
               "('Hardy','SS',22,78,11,19,7,0,2,8,13,0.244),"
               "('Jones','CF',47,181,23,43,8,0,5,23,38,0.238),"
               "('Davis','1B',51,186,37,41,10,0,10,28,70,0.22),"
               "('Alvarez','DH',36,108,7,23,8,0,3,12,28,0.213),"
               "('Flaherty','3B',28,67,5,13,2,0,0,4,22,0.194),"
               "('Joseph','C',23,66,5,12,2,0,0,0,14,0.182),"
               "('Janish','SS',7,17,1,2,1,0,0,0,2,0.118);")

connection.commit()

cursor.execute("select * from batting_avg")
results = cursor.fetchall()
for row in results:
    print(row)

cursor.close()
connection.close()

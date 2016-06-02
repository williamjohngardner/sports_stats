import psycopg2

connection = psycopg2.connect("dbname=orioles_stats user=billgardner")
cursor = connection.cursor()


def player_name_search():
    search = input("Enter a name to search: ")
    cursor.execute("select * from batting_avg where name = %s;", (search, ))
    data = cursor.fetchall()
    print(data)


def player_insert():
    name = input("Insert name: ")
    position = input("Insert position: ")
    games = input("Insert No. of games played: ")
    at_bats = input("Insert No of at bats: ")
    runs = input("runs")
    hits = input("hits")
    doubles = input("doubles")
    triples = input("triples")
    home_runs = input("home_runs")
    rbi = input("rbi")
    strike_outs = input("strike outs")
    average = input("average")

    cursor.execute("insert into batting_avg values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (name, position,
                   games, at_bats, runs, hits, doubles, triples, home_runs, rbi, strike_outs, average))

player_name_search()

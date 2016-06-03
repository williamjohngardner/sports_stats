import psycopg2

connection = psycopg2.connect("dbname=orioles_stats user=billgardner")
cursor = connection.cursor()


def search_criteria():
    print("Welcome to the Baltimore Orioles' Batting Average Database.")
    user_prompt = input("How would you like to search the database?"
                        "\n (N)ame | (P)osition | (B)atting Average").lower()
    if user_prompt == "n":
        name = input("Please enter the name to search: ").capitalize()
        cursor.execute("select * from batting_avg where name = %s;", (name, ))
        data = cursor.fetchall()
        print(data)
    elif user_prompt == "p":
        position = input("Please enter the position to search (ie. 1B, 2B, CF, P, etc.): ").upper()
        cursor.execute("select * from batting_avg where position = %s;", (position, ))
        data = cursor.fetchall()
        print(data)
    elif user_prompt == "b":
        bat_avg = input("Please enter a batting average and see which players' average are above: ")
        cursor.execute("select * from batting_avg where average > %s;", (bat_avg, ))
        data = cursor.fetchall()
        print(data)
    else:
        print("Invalid entry")


def player_name_search():
    search = input("Enter a name to search: ")
    cursor.execute("select * from batting_avg where name = %s;", (search, ))
    data = cursor.fetchall()
    print(data)


def player_insert():

    name = input("Insert player's name: ")
    position = input("Insert player's position: ")
    games = input("Insert No. of games played: ")
    at_bats = input("Insert No. of at bats: ")
    runs = input("Insert No. of runs: ")
    hits = input("Insert No. of hits: ")
    doubles = input("Insert No. of doubles: ")
    triples = input("Insert No. of triples: ")
    home_runs = input("Insert No. of home runs: ")
    rbi = input("Insert No. of RBIs: ")
    strike_outs = input("Insert No. of strike outs: ")
    average = input("Insert player's batting average: ")

    cursor.execute("insert into batting_avg values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (name, position,
                   games, at_bats, runs, hits, doubles, triples, home_runs, rbi, strike_outs, average))

    connection.commit()
    print("Your new Player Record has been successfully added.")

player_insert()

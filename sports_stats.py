import psycopg2

connection = psycopg2.connect("dbname=orioles_stats user=billgardner")
cursor = connection.cursor()


def search_menu():
    print("Welcome to a Baltimore Orioles' Database.")
    choice = input("Would you like to (S)earch or (A)dd a new player to the database?").lower()
    if choice == "s":
        search_criteria()
    elif choice == "a":
        player_insert()


def search_criteria():
    user_prompt = input("How would you like to search the database?"
                        "\n (N)ame | (P)osition | (B)atting Average | (M)ain Menu").lower()
    if user_prompt == "n":
        name_search()
    elif user_prompt == "p":
        position_search()
    elif user_prompt == "b":
        bat_avg_search()
    elif user_prompt == "m":
        search_menu()
    else:
        print("Invalid entry")
        search_criteria()


def name_search():
    search = input("Enter a name to search: ")
    cursor.execute("select * from batting_avg where name = %s;", (search, ))
    data = cursor.fetchall()
    print(data)
    upd_name = input("Would you like to update this player's name? (Y)es or (N)o:").lower()
    if upd_name == "y":
        update_record()
    elif upd_name == "n":
        search_criteria()


def position_search():
    position = input("Please enter the position to search (ie. 1B, 2B, CF, P, etc.): ").upper()
    cursor.execute("select * from batting_avg where position = %s;", (position,))
    data = cursor.fetchall()
    print(data)
    upd_name = input("Would you like to update this player's position? (Y)es or (N)o:").lower()
    if upd_name == "y":
        update_record()
    elif upd_name == "n":
        search_criteria()


def bat_avg_search():
    bat_avg = input("Please enter a batting average and see which players' average are above: ")
    cursor.execute("select * from batting_avg where average > %s;", (bat_avg,))
    data = cursor.fetchall()
    print(data)
    upd_name = input("Would you like to update this player's batting average? (Y)es or (N)o:").lower()
    if upd_name == "y":
        update_record()
    elif upd_name == "n":
        search_criteria()


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
    search_menu()


def update_record():
    update = input("Which record do you want to update? "
                   "\n (N)ame | (P)osition | (B)atting Average").lower()
    if update == "n":
        name = input("Enter the name you want to update: ")
        updated_name = input("Enter the new name: ")
        cursor.execute("update batting_avg set name = %s where name = %s", (updated_name, name))
        connection.commit()
    elif update == "p":
        position_search()
    elif update == "b":
        bat_avg_search()
    else:
        print("Invalid entry.")
        update_record()
    search_menu()


def order_by():
    cursor.execute("select * from batting_avg order by average desc;")
    data = cursor.fetchall()
    print(data)

order_by()

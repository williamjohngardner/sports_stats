import psycopg2

connection = psycopg2.connect("dbname=orioles_stats user=billgardner")
cursor = connection.cursor()


def search_menu():
    print("Welcome to a Baltimore Orioles' Database.")
    choice = input("Would you like to (S)earch or (A)dd a new player (U)pdate a player or (E)xit the database?").lower()
    if choice == "s":
        search_criteria()
    elif choice == "a":
        player_insert()
    elif choice == "u":
        update_record()
    elif choice == "e":
        print("Goodbye")
        cursor.close()
        connection.close()
        exit()
    else:
        print("Invalid Entry")
        search_menu()


def search_criteria():
    user_prompt = input("How would you like to search the database?"
                        "\n (N)ame | (P)osition | (R)BI | (B)atting Average | (T)op Stats | (M)ain Menu").lower()
    if user_prompt == "n":
        name_search()
    elif user_prompt == "p":
        position_search()
    elif user_prompt == "b":
        bat_avg_search()
    elif user_prompt == "m":
        search_menu()
    elif user_prompt == "t":
        order_by()
    else:
        print("Invalid entry")
        search_criteria()


def name_search():
    search = input("Enter a name to search: ")
    cursor.execute("select * from batting_avg where name = %s;", (search, ))
    data = cursor.fetchall()
    print(data)
    upd_name = input("Would you like to update this player's stats? (Y)es or (N)o:").lower()
    if upd_name == "y":
        update_record()
    elif upd_name == "n":
        search_criteria()


def position_search():
    position = input("Please enter the position to search (ie. 1B, 2B, CF, P, etc.): ").upper()
    cursor.execute("select * from batting_avg where position = %s;", (position,))
    data = cursor.fetchall()
    print(data)
    upd_name = input("Would you like to update this player's stats? (Y)es or (N)o:").lower()
    if upd_name == "y":
        update_record()
    elif upd_name == "n":
        search_criteria()


def bat_avg_search():
    bat_avg = input("Please enter a batting average and see which players' average are above: ")
    cursor.execute("select * from batting_avg where average > %s;", (bat_avg,))
    data = cursor.fetchall()
    print(data)
    upd_name = input("Would you like to update this player's stats? (Y)es or (N)o:").lower()
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
    name = input("Enter the name of the record you wish to update: ")
    field = input("Which field do you want to update? (N)ame, (P)osition, (B)atting Avg").lower()
    if field == "n":
        field = 'name'
        new_field = input("Please enter the new name")
        cursor.execute("update batting_avg set name = %s where name = %s", (new_field, name))
        connection.commit()
    elif field == "p":
        field = 'position'
        new_field = input("Please enter the new position")
        cursor.execute("update batting_avg set position = %s where name = %s", (new_field, name))
        connection.commit()
    elif field == "b":
        field = 'average'
        new_field = input("Please enter the new batting average")
        cursor.execute("update batting_avg set average = %s where name = %s", (new_field, name))
        connection.commit()
    else:
        print("Invalid entry")
        update_record()

    search_menu()


def order_by():
    search = input("Search for top five players stats by category: Batting (A)verage, Home(R)uns, (H)it, (D)oubles, "
                   "(T)riples, (R)BI, (S)trike outs").lower()
    if search == "a":
        cursor.execute("select * from batting_avg order by average desc limit 5;")
    elif search == "r":
        cursor.execute("select * from batting_avg order by home_runs desc limit 5;")
    elif search == "h":
        cursor.execute("select * from batting_avg order by hits desc limit 5;")
    elif search == "d":
        cursor.execute("select * from batting_avg order by doubles desc limit 5;")
    elif search == "t":
        cursor.execute("select * from batting_avg order by triples desc limit 5;")
    elif search == "r":
        cursor.execute("select * from batting_avg order by rbi desc limit 5;")
    elif search == "s":
        cursor.execute("select * from batting_avg order by strike_outs desc limit 5;")
    data = cursor.fetchall()
    print(data)

update_record()

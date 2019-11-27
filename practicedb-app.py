import psycopg2

try:
    # connect to db and create cursor
    connection = psycopg2.connect(user="postgres",
                                  password="password",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="practicedb")
    cursor = connection.cursor()

    # create table in existing database called 'practice_table'
    cursor.execute("CREATE TABLE ivans_favorites ("
                   "beer varchar,"
                   "car varchar,"
                   "game varchar,"
                   "number integer);")

    # insert data into newly created table
    # cursor.execute("INSERT INTO ivans_favorites (beer, car, game, number)"
    #                "VALUES ('Trois', 'Skyline', 'Last of Us', 17);")

    connection.commit()
    connection.close()
    cursor.close()

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL database", error)

finally:
    print("PostgreSQL database connection is now closed.")

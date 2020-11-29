# Proyecto 4
# Computacion en la Nube
# Samuel Perez
import psycopg2

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "postgressam",
                                  host = "dbproy4.ca5eltzpchaz.us-east-1.rds.amazonaws.com",
                                  port = "5432",
                                  database = "dbproy4")

    cursor = connection.cursor()

    print("Connected to dbproy4 \n")
    # creating table courses_macc
    sql_input_create = "CREATE TABLE courses_macc(name varchar(40), credits integer);"
    cursor.execute(sql_input_create)
    connection.commit()

    print("courses_macc table created")

    # inserting record
    sql_input_insert = " INSERT INTO courses_macc VALUES (%s,%s)"
    values = ('cloud computing', 2)
    cursor.execute(sql_input_insert, values)
    connection.commit()

    count = cursor.rowcount
    print (count, "record inserted")

    # inserting record
    values = ('topology', 3)
    cursor.execute(sql_input_insert, values)
    connection.commit()

    count = cursor.rowcount
    print (count, "record inserted")
    
    # query
    sql_input_query = "SELECT * FROM courses_macc"
    cursor.execute(sql_input_query)
    records = cursor.fetchall() 

    print("\nRecords in table courses_macc:")
    for r in records:
        print (r)

except (Exception, psycopg2.Error) as error:
    print ("\nError in connection", error)

finally:
        if(connection):
            cursor.close()
            connection.close()
            print("\nConnection is closed")
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
    
    # query
    sql_input_query = "SELECT * FROM saberpro_2019_2"
    cursor.execute(sql_input_query)
    records = cursor.fetchall() 

    print("\nFirst record in table saberpro_2019_2:")
    print(records[0])

except (Exception, psycopg2.Error) as error:
    print ("\nError in connection", error)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print("\nConnection is closed")
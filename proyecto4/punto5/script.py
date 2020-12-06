# Proyecto 4
# Computacion en la Nube
# Samuel Perez
import psycopg2

try:
    connection_master = psycopg2.connect(user = "postgres",
                                  password = "postgressam",
                                  host = "dbproy4.ca5eltzpchaz.us-east-1.rds.amazonaws.com",
                                  port = "5432",
                                  database = "dbproy4")

    connection_replica = psycopg2.connect(user = "postgres",
                                  password = "postgressam",
                                  host = "dbproy4a.ca5eltzpchaz.us-east-1.rds.amazonaws.com",
                                  port = "5432",
                                  database = "dbproy4")

    cursor_master = connection_master.cursor()
    print("Connected to dbproy4 MASTER\n")

    cursor_replica = connection_replica.cursor()
    print("Connected to dbproy4 REPLICA\n")
    
    # query master
    sql_input_query = "SELECT * FROM saberpro_2019_2"
    cursor_master.execute(sql_input_query)
    records = cursor_master.fetchall() 

    print("\nFirst record in table saberpro_2019_2: (MASTER)")
    print(records[0])

    # query master
    sql_input_query = "SELECT * FROM saberpro_2019_2"
    cursor_replica.execute(sql_input_query)
    records = cursor_replica.fetchall() 

    print("\nFirst record in table saberpro_2019_2: (REPLICA)")
    print(records[0])

except (Exception, psycopg2.Error) as error:
    print ("\nError in connection", error)

finally:
    if(connection_master):
        cursor_master.close()
        connection_master.close()
        print("\nConnection MASTER is closed")

    if(connection_replica):
        cursor_replica.close()
        connection_replica.close()
        print("\nConnection REPLICA is closed")
import mysql.connector
from mysql.connector import errorcode

def create_database():
  cnx = None
  cursor = None
  database = alx_book_store

  try:
    cnx = mysql.connector(
      host="localhost",
      user="root", 
      password="Navalayo@1970"
    )
    cursor = cnx.cursor()
    create_database = f"CREATE DATABASE IF NOT EXISTS {database}"
    cursor.execute(create_database)
    print(f"Database '{database_name}' created successfully!")
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Failed to connect to the database. Check your username and password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(f"Error: Database '{database_name}' does not exist (and couldn't be created for some reason).")
    else:
        print(f"An unexpected error occurred: {err}")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
  finally:
    if cursor:
        cursor.close()
    if cnx and cnx.is_connected():
        cnx.close()

    
    

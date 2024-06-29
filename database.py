""" This module contains the functions to interact with the database. """

import sqlite3
from sqlite3 import Error



def execute_query(query):
    """   """
    try:
        connection = sqlite3.connect("library_db.sqlite")
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        #print(f"Query executed successfully")
        cursor.close()
        connection.close()
    except Error as e:
        print(f"The error '{e}' occured while executing a query to the database.")

        
def execute_read_query(query) -> list:    
    try:
        connection = sqlite3.connect("library_db.sqlite")
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        #print(f"This is the result: {result}!")
        cursor.close()
        connection.close()
        return result
    except Error as e:
        print(f"The error '{e}' occured while executing a read query to the database.")
        return []
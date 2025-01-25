import sqlite3

connection = sqlite3.connect("./my-database.db")
cursor = connection.cursor()

asghar = """
 CREATE TABLE IF NOT EXISTS user (
 userId INTEGER ,
 name VARCHAR (60),
 family VARCHAR (60),
 email VARCHAR (60)
 );
"""
cursor.execute(asghar)
connection.commit()
connection.close()
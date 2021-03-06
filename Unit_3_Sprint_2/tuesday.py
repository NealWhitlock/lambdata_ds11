import os
from dotenv import load_dotenv
import psycopg2

load_dotenv() #> loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

print("CONNECTING TO THE DATABASE...")

### Connect to ElephantSQL-hosted PostgreSQL
connection = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, 
    password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

### A "cursor", a structure to iterate over db records to perform queries
cursor = connection.cursor()
print("CURSOR:", cursor)

### An example query
cursor.execute('SELECT * from test_table;')
result = cursor.fetchall()
print("RESULT TYPE:", type(result))
print("RESULT:",result)




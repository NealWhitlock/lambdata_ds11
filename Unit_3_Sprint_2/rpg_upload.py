import os
from dotenv import load_dotenv
import psycopg2
import sqlite3

load_dotenv() #> loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

sql_connection = sqlite3.connect('rpg_db.sqlite3')
sql_cursor = sql_connection.cursor()

# Get characters
query = 'SELECT * FROM charactercreator_character'
characters = sql_cursor.execute(query).fetchall()

### Connect to ElephantSQL-hosted PostgreSQL
postg_connection = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, 
    password=DB_PASSWORD, host=DB_HOST)

### A "cursor", a structure to iterate over db records to perform queries
postg_cursor = postg_connection.cursor()

# Create a new table
query = """
CREATE TABLE IF NOT EXISTS charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name varchar,
    level int,
    exp int,
    hp int,
    strength int,
    intelligence int,
    dexterity int,
    wisdom int
);
"""
postg_cursor.execute(query)

# Insert the characters
for character in characters:
    insert_query = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:])
    postg_cursor.execute(insert_query)

postg_cursor.close()
postg_connection.commit()

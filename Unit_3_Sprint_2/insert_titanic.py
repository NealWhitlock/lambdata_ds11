import os
from dotenv import load_dotenv
import psycopg2
import pandas as pd

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

# TODO: Create a new table
query = """
CREATE TABLE IF NOT EXISTS passengers (
    id SERIAL PRIMARY KEY,
    survived int,
    pclass int,
    name varchar,
    sex varchar,
    age int,
    sib_spouse_count int,
    parent_child_count int,
    fare float8
);
"""

cursor.execute(query)

connection.commit()

# TODO: Read CSV contents and insert into a new table
df = pd.read_csv('titanic.csv')
print(df.head())
for i in range(len(df)):
    survived = df.iloc[i][0]
    pclass = df.iloc[i][1]
    name = df.iloc[i][2]
    sex = df.iloc[i][3]
    age = df.iloc[i][4]
    sib_count = df.iloc[i][5]
    par_count = df.iloc[i][6]
    far = df.iloc[i][7]
    values = f"({survived}, {pclass}, '{name}', '{sex}', {age}, {sib_count}, {par_count}, {far})"
    query = "INSERT INTO passengers VALUES " + values
    cursor.execute(query)

connection.commit()

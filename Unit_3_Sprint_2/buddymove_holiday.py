import numpy as np
import pandas as pd
import sqlite3

url = 'https://raw.githubusercontent.com/NealWhitlock/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv'

df = pd.read_csv(url)
print(df.shape)
print(df.head())

connection = sqlite3.connect("buddymove_holidayiq.sqlite3")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS review
                  ([generated_id] INTEGER PRIMARY KEY, [User Id] text, 
                  [Sports] integer, [Religious] integer, [Nature] integer,
                  [Theatre] integer, [Shopping] integer, [Picnic] integer)""")

connection.commit()

df.to_sql('review', connection, if_exists='replace')

# Count how many rows you have.
query = """
SELECT
    count('User Id')
FROM review
"""
result = cursor.execute(query)
num_rows = cursor.fetchone()
print('-'*40)
print(f"There are {num_rows[0]} rows in the database.")
print('-'*40)

# How many users who reviewed at least 100 Nature in the 
# category also reviewed at least 100 in the Shopping category?
query = """
SELECT
	(Nature > 99) as nature_100,
	(Shopping > 99) as shopping_100
FROM review
"""
result = cursor.execute(query)
count = 0
for row in result:
    if (row[0] == 1) and (row[1] == 1):
        count += 1
print(f"There are {count} times that Nature and Shopping are 100 or above together.")
print('-'*40)

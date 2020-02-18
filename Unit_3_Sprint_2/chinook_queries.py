import os
import sqlite3

#DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "chinook.db")

connection = sqlite3.connect("chinook.db")

print("Connection:", connection)

cursor = connection.cursor()
print("Cursor:", cursor)

query = """
SELECT
  Country
  ,count(distinct CustomerId) as CustomerCount -- > 59
FROM customers
GROUP BY Country
ORDER BY CustomerCount DESC
LIMIT 5
"""

result = cursor.execute(query)
print("Result", result)

result2 = cursor.execute(query).fetchall()
print("Result 2:", result2)

for row in result2:
    print(type(row))
    print(row)
    print(row[0])
    print(row[1])
    # print(row["Country"])
    # print(row["CustomerCount"])
    print("-----")

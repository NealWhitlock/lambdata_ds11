import sqlite3

# === SETUP ===

# Create the connection and the cursor
connection = sqlite3.connect("chinook.db")
cursor = connection.cursor()
print("="*40)

# === QUERIES ===

# Find the average invoice total for each customer, 
# return the details for the first 5 ID's
query1 = """
SELECT AVG(total) as average, CustomerId 
    FROM invoices 
    GROUP BY CustomerId 
    ORDER BY average DESC
    LIMIT 5
"""
averages = cursor.execute(query1).fetchall()
for ave in averages:
    print(f"Customer {ave[1]} had an average of ${ave[0]:.2f}")
print("="*40)

# Return all columns in Customer for the first 5 
# customers residing in the United States
query2 = """
    SELECT *
    FROM customers 
    WHERE country = 'USA' 
    LIMIT 5
"""
staters = cursor.execute(query2).fetchall()
for person in staters:
    print(person)
print("="*40)

# Which employee does not report to anyone?
query3 = """
SELECT FirstName, LastName
    FROM employees
    WHERE ReportsTo IS NULL
"""
rogue = cursor.execute(query3).fetchone()
print(f"{rogue[0]} {rogue[1]} answers to no one!")
print("="*40)

# Find the number of unique composers
query4 = """
SELECT COUNT(DISTINCT Composer)
    FROM tracks
"""
composer = cursor.execute(query4).fetchone()
print(f"There are {composer[0]} unique composers listed.")
print("="*40)

# How many rows are in the Track table?
query5 = """
SELECT COUNT(TrackId)
    FROM tracks
"""
tracks = cursor.execute(query5).fetchone()
print(f"There are {tracks[0]} tracks.")
print("="*40)

# === JOINS ===

# Get the name of all Black Sabbath tracks and the albums 
# they came off of
query6 = """
SELECT albums.Title, tracks.Name 
    FROM albums
	JOIN tracks
	ON albums.AlbumId = tracks.AlbumId
	WHERE albums.AlbumId = 16 or albums.AlbumId = 17
"""
sabbath = cursor.execute(query6).fetchall()
for track in sabbath:
    print(f"Track '{track[1]}' is on the {track[0]} album.")
print("="*40)

# What is the most popular genre by number of tracks?
query7 = """
SELECT COUNT(tracks.GenreID) as tally, tracks.GenreId, genres.Name
	FROM tracks
	JOIN genres
	ON tracks.GenreId = genres.GenreId
	GROUP BY tracks.GenreId
	ORDER BY tally DESC
"""
pop = cursor.execute(query7).fetchone()
print(f"The most popular genre was {pop[2]} with {pop[0]} total tracks.")
print("="*40)

# Find all customers that have spent over $45
query8 = """
SELECT invoices.CustomerId, SUM(invoices.Total) as totes, 
customers.FirstName, customers.LastName
	FROM invoices
	LEFT JOIN customers
	ON invoices.CustomerId = customers.CustomerId
	GROUP BY invoices.CustomerId
	HAVING totes > 45
	ORDER BY totes DESC
"""
big_spenders = cursor.execute(query8).fetchall()
for person in big_spenders:
    print(f"{person[2]} {person[3]} spent ${person[1]:.2f}.")
print("="*40)

# Find the first and last name, title, and the number of 
# customers each employee has helped. If the customer 
# count is 0 for an employee, it doesn't need to be displayed. 
# Order the employees from most to least customers.
query9 = """
SELECT customers.SupportRepId, employees.EmployeeId, employees.FirstName, employees.LastName, employees.Title, COUNT(*)
	FROM employees
	JOIN customers
	ON customers.SupportRepId = employees.EmployeeId
	GROUP BY employees.EmployeeId
	ORDER BY COUNT(*) DESC
"""
helpers = cursor.execute(query9).fetchall()
for helper in helpers:
    print(f"{helper[2]} {helper[3]} helped {helper[5]} people as a {helper[4]}")
print("="*40)

# Return the first and last name of each employee and who 
# they report to
query10 = """
SELECT emp.FirstName, emp.LastName, emp.EmployeeId, emp.ReportsTo, 
rep.FirstName, rep.LastName
	FROM employees emp
	LEFT JOIN employees rep
	ON emp.ReportsTo = rep.EmployeeId
"""
report = cursor.execute(query10).fetchall()
for rep in report:
    if rep[4] == None:
        print(f"{rep[0]} {rep[1]} reports to NO ONE!")
    else:
        print(f"{rep[0]} {rep[1]} reports to {rep[4]} {rep[5]}")
print("="*40)

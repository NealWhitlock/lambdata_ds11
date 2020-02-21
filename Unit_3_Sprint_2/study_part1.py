import sqlite3


# Create the connection and the cursor
connection = sqlite3.connect("study_part1.sqlite3")
cursor = connection.cursor()

# Create a query to create the table and insert values
creation_query = """
CREATE TABLE IF NOT EXISTS students (
    student TEXT,
    studied TEXT,
    grade INT,
    age INT,
    sex TEXT
)
"""

insertion_query = """
INSERT INTO students
    (student, studied, grade, age, sex)
VALUES 
    ('Lion-O', 'True', 85, 24, 'Male'),
    ('Cheetara', 'True', 95, 22, 'Female'),
    ('Mumm-Ra', 'False', 65, 153, 'Male'),
    ('Snarf', 'False', 70, 15, 'Male'),
    ('Panthro', 'True', 80, 30, 'Male')
"""

cursor.execute(creation_query)
cursor.execute(insertion_query)

# Commit the queries to save the table
connection.commit()

# What is the average age? 
# Expected Result - 48.8
ave_age_query = """
SELECT AVG(age) FROM students;
"""
age = cursor.execute(ave_age_query).fetchone()
print("Average age:", age[0])

# What are the names of the female students? 
# Expected Result - 'Cheetara'
female_query = """
SELECT student FROM students WHERE sex = 'Female'
"""
females = cursor.execute(female_query).fetchall()
print("Females:") 
for person in females:
    print(person[0])

# How many students studied? 
# Expected Results - 3
study_query = """
SELECT COUNT(studied) FROM students WHERE studied = "True"
"""
studied = cursor.execute(study_query).fetchone()
print("Number of students that studied:", studied[0])

# Return all students and all columns, 
# sorted by student names in alphabetical order.
ordered_query = """
SELECT * FROM students ORDER BY student;
"""
ordered = cursor.execute(ordered_query).fetchall()
#print(ordered)
for person in ordered:
    print(person)

cursor.close()
connection.close()

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

### Connect to ElephantSQL-hosted PostgreSQL
postg_connection = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, 
    password=DB_PASSWORD, host=DB_HOST)

### A "cursor", a structure to iterate over db records to perform queries
postg_cursor = postg_connection.cursor()

# Get characters
query = 'SELECT * FROM charactercreator_character'
characters = sql_cursor.execute(query).fetchall()

# Create a new table for characters
character_query = """
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
postg_cursor.execute(character_query)

# Insert the characters into character table
for character in characters:
    insert_query = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:])
    postg_cursor.execute(insert_query)

# Get character inventory
query = 'SELECT * FROM charactercreator_character_inventory'
inventory = sql_cursor.execute(query).fetchall()

# Create new table for character inventory
inventory_query = """
CREATE TABLE IF NOT EXISTS charactercreator_character_inventory (
    id SERIAL PRIMARY KEY,
    character_id int,
    item_id int
);
"""
postg_cursor.execute(inventory_query)

# Insert inventory data into inventory table
for item in inventory:
    insert_query = """
    INSERT INTO charactercreator_character_inventory
    (character_id, item_id)
    VALUES """ + str(item[1:])
    postg_cursor.execute(insert_query)

# Get armory items
query = 'SELECT * FROM armory_item'
armory_item = sql_cursor.execute(query).fetchall()

# Create new table for armory items
armory_item_query = """
CREATE TABLE IF NOT EXISTS armory_item (
    item_id SERIAL PRIMARY KEY,
    name varchar,
    value int,
    weight int
);
"""
postg_cursor.execute(armory_item_query)

# Insert data into armory items table
for item in armory_item:
    insert_query = """
    INSERT INTO armory_item
    (name, value, weight)
    VALUES """ + str(item[1:])
    postg_cursor.execute(insert_query)

# Get armory weapons items
query = 'SELECT * FROM armory_weapon'
armory_weapon = sql_cursor.execute(query).fetchall()

# Create new table for armory weapon
armory_weapon_query = """
CREATE TABLE IF NOT EXISTS armory_weapon (
    item_ptr_id SERIAL PRIMARY KEY,
    power int
);
"""
postg_cursor.execute(armory_weapon_query)

# Insert data into armory items table
for item in armory_weapon:
    insert_query = """
    INSERT INTO armory_weapon
    (item_ptr_id, power)
    VALUES """ + str(item)
    postg_cursor.execute(insert_query)

# Get fighter info
query = 'SELECT * FROM charactercreator_fighter'
fighters = sql_cursor.execute(query).fetchall()

# Create new table for fighters
fighter_query = """
CREATE TABLE IF NOT EXISTS charactercreator_fighter (
    character_ptr_id SERIAL PRIMARY KEY,
    using_shield int,
    rage int
);
"""
postg_cursor.execute(fighter_query)

# Insert data into fighters table
for fighter in fighters:
    insert_query = """
    INSERT INTO charactercreator_fighter
    (character_ptr_id, using_shield, rage)
    VALUES """ + str(fighter)
    postg_cursor.execute(insert_query)

# Get mage info
query = 'SELECT * FROM charactercreator_mage'
mages = sql_cursor.execute(query).fetchall()

# Create new table for mages
mage_query = """
CREATE TABLE IF NOT EXISTS charactercreator_mage (
    character_ptr_id SERIAL PRIMARY KEY,
    has_pet int,
    mana int
);
"""
postg_cursor.execute(mage_query)

# Insert data into mage table
for mage in mages:
    insert_query = """
    INSERT INTO charactercreator_mage
    (character_ptr_id, has_pet, mana)
    VALUES """ + str(mage)
    postg_cursor.execute(insert_query)

# Get cleric info
query = 'SELECT * FROM charactercreator_cleric'
clerics = sql_cursor.execute(query).fetchall()

# Create new table for clerics
clerics_query = """
CREATE TABLE IF NOT EXISTS charactercreator_cleric (
    character_ptr_id SERIAL PRIMARY KEY,
    using_shield int,
    mana int
);
"""
postg_cursor.execute(clerics_query)

# Insert data into clerics table
for cleric in clerics:
    insert_query = """
    INSERT INTO charactercreator_cleric
    (character_ptr_id, using_shield, mana)
    VALUES """ + str(cleric)
    postg_cursor.execute(insert_query)

# Get thief info
query = 'SELECT * FROM charactercreator_thief'
thieves = sql_cursor.execute(query).fetchall()

# Create new table for thieves
thief_query = """
CREATE TABLE IF NOT EXISTS charactercreator_thief (
    character_ptr_id SERIAL PRIMARY KEY,
    is_sneaking int,
    energy int
);
"""
postg_cursor.execute(thief_query)

# Insert data into thief table
for thief in thieves:
    insert_query = """
    INSERT INTO charactercreator_thief
    (character_ptr_id, is_sneaking, energy)
    VALUES """ + str(thief)
    postg_cursor.execute(insert_query)

# Get necromancer info
query = 'SELECT * FROM charactercreator_necromancer'
necromancers = sql_cursor.execute(query).fetchall()

# Create new table for necromancer
necromancer_query = """
CREATE TABLE IF NOT EXISTS charactercreator_necromancer (
    mage_ptr_id SERIAL PRIMARY KEY,
    talisman_charged int
);
"""
postg_cursor.execute(necromancer_query)

# Insert data into necromancer table
for necromancer in necromancers:
    insert_query = """
    INSERT INTO charactercreator_necromancer
    (mage_ptr_id, talisman_charged)
    VALUES """ + str(necromancer)
    postg_cursor.execute(insert_query)

postg_cursor.close()
postg_connection.commit()

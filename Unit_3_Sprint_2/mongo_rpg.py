import os
import pymongo
import sqlite3
from dotenv import load_dotenv

load_dotenv()

# Get SQL connection and cursor set up
sql_connection = sqlite3.connect('rpg_db.sqlite3')
sql_cursor = sql_connection.cursor()

# Get confifentials
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASS = os.getenv("MONGO_PASS")
MONGO_SERVER = os.getenv("MONGO_SERVER")

# Get Mongo connections set up
client = pymongo.MongoClient(f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_SERVER}/test?retryWrites=true&w=majority")
db = client.rpg_db

# Get character info from SQL
query = 'SELECT * FROM charactercreator_character'
characters = sql_cursor.execute(query).fetchall()

# Create character entries and insert each one into collection
chars = []
for character in characters:
    char_dict = {
        'character_id': character[0],
        'name': character[1],
        'level': character[2],
        'exp': character[3],
        'hp': character[4],
        'strength': character[5],
        'intelligence': character[6],
        'dexterity': character[7],
        'wisdom': character[8]
    }
    chars.append(char_dict)
# Add all of the characters
db.charactercreator_character.insert_many(chars)
print("characters uploaded")


# Get character inventory
query = 'SELECT * FROM charactercreator_character_inventory'
inventory = sql_cursor.execute(query).fetchall()

# Create character entries and insert each one into collection
inv_items = [] # House the item dictionaries
for item in inventory:
    item_dict = {
        'id': item[0],
        'character_id': item[1],
        'item_id': item[2]
    }
    inv_items.append(item_dict)
# Add the items
db.charactercreator_character_inventory.insert_many(inv_items)
print("character inventory uploaded")


# Get armory items
query = 'SELECT * FROM armory_item'
armory_item = sql_cursor.execute(query).fetchall()

# Create armory item entries and insert each one into collection
arm_items = []
for item in armory_item:
    item_dict = {
        'item_id': item[0],
        'name': item[1],
        'value': item[2],
        'weight': item[3]
    }
    arm_items.append(item_dict)
# Add the armory items
db.armory_item.insert_many(arm_items)
print("armory items uploaded")


# Get armory weapons items
query = 'SELECT * FROM armory_weapon'
armory_weapon = sql_cursor.execute(query).fetchall()

weapons_list = []
for weapon in armory_weapon:
    weapon_dict = {
        'item_ptr_id': weapon[0],
        'power': weapon[1]
    }
    weapons_list.append(weapon_dict)
db.armory_weapon.insert_many(weapons_list)
print("armory weapons uploaded")


# Get fighter info
query = 'SELECT * FROM charactercreator_fighter'
fighters = sql_cursor.execute(query).fetchall()

fighter_list =[]
for fighter in fighters:
    fighter_dict = {
        'character_ptr_id': fighter[0],
        'using_shield': fighter[1],
        'rage': fighter[2]
    }
    fighter_list.append(fighter_dict)
db.charactercreator_fighter.insert_many(fighter_list)
print("fighters uploaded")


# Get mage info
query = 'SELECT * FROM charactercreator_mage'
mages = sql_cursor.execute(query).fetchall()

mage_list = []
for mage in mages:
    mage_dict = {
        'character_ptr_id': mage[0],
        'has_pet': mage[1],
        'mana': mage[2]
    }
    mage_list.append(mage_dict)
db.charactercreator_mage.insert_many(mage_list)
print("mages uploaded")


# Get cleric info
query = 'SELECT * FROM charactercreator_cleric'
clerics = sql_cursor.execute(query).fetchall()

cleric_list = []
for cleric in clerics:
    cleric_dict = {
        'character_ptr_id': cleric[0],
        'using_shield': cleric[1],
        'mana': cleric[2]
    }
    cleric_list.append(cleric_dict)
db.charactercreator_cleric.insert_many(cleric_list)
print("clerics uploaded")


# Get thief info
query = 'SELECT * FROM charactercreator_thief'
thieves = sql_cursor.execute(query).fetchall()

thief_list = []
for thief in thieves:
    thief_dict = {
        'character_ptr_id': thief[0],
        'is_sneaking': thief[1],
        'energy': thief[2]
    }
    thief_list.append(thief_dict)
db.charactercreator_thief.insert_many(thief_list)
print("thieves uploaded")


# Get necromancer info
query = 'SELECT * FROM charactercreator_necromancer'
necromancers = sql_cursor.execute(query).fetchall()

necromancer_list = []
for necromancer in necromancers:
    necro_dict = {
        'mage_ptr_id': necromancer[0],
        'talisman_charged': necromancer[1],
    }
    necromancer_list.append(necro_dict)
db.charactercreator_necromancer.insert_many(necromancer_list)
print("necromancers uploaded")




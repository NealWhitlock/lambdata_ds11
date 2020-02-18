import sqlite3

connection = sqlite3.connect("rpg_db.sqlite3")

cursor = connection.cursor()

# How many characters are in the character table?
query1 = """
SELECT
	count(DISTINCT character_id)
FROM charactercreator_character
"""

result1 = cursor.execute(query1)
num = cursor.fetchone()
print("Number of characters:", num[0])
print('-'*40)

# How many characters in each subclass?
subclasses = ['cleric', 'fighter', 'mage', 'necromancer', 'thief']
for s_class in subclasses:
    word = 'character'
    if s_class == 'necromancer':
        word = 'mage'
    query = f"""
    SELECT
        count(DISTINCT {word}_ptr_id)
    FROM charactercreator_{s_class}
    """
    result = cursor.execute(query)
    num = cursor.fetchone()
    print(f"Number of characters in {s_class} subclass:", num[0])
print('-'*40)

# How many items are there?
query2 = """
SELECT
	count(DISTINCT item_id)
FROM armory_item
"""

result1 = cursor.execute(query2)
num = cursor.fetchone()
print("Number of items:", num[0])
print('-'*40)

# How many of the items are weapons? How many are not?
query3 = """
SELECT
	count(DISTINCT item_ptr_id)
FROM armory_weapon
"""

result2 = cursor.execute(query3)
num_2 = cursor.fetchone()
print("Number of weapons:", num_2[0])
print("Number of non-weapon items:", num[0] - num_2[0])
print('-'*40)

# How many items does each character have?
query4 = """
SELECT
	character_id,
	count(DISTINCT item_id) as item_count
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20
"""
result = cursor.execute(query4)
for row in result:
    print(f"Character {row[0]} has {row[1]} item(s).")
print('-'*40)

# How many weapons does each character have?
query5 = """
SELECT
	charactercreator_character_inventory.character_id,
	charactercreator_character_inventory.item_id,
	armory_weapon.item_ptr_id,
	COUNT(charactercreator_character_inventory.item_id) as weapons
FROM charactercreator_character_inventory
JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY charactercreator_character_inventory.character_id
LIMIT 20
"""
result = cursor.execute(query5)
for row in result:
    print(f"Character {row[0]} has {row[3]} weapon(s).")
print('-'*40)

# On average, how many items does each character have?
query6 = """
SELECT
	character_id,
	count(DISTINCT item_id) as item_count
FROM charactercreator_character_inventory
GROUP BY character_id
"""
result = cursor.execute(query6)
total_items = 0
count = 0
for row in result:
    total_items += row[1]
    count += 1
print(f"On average, each character has {(total_items/count):.2f} items.")
print('-'*40)

# On average, how many weapons does each character have?
query7 = """
SELECT
	charactercreator_character_inventory.character_id,
	charactercreator_character_inventory.item_id,
	armory_weapon.item_ptr_id,
	COUNT(charactercreator_character_inventory.item_id) as weapons
FROM charactercreator_character_inventory
JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY charactercreator_character_inventory.character_id
"""
result = cursor.execute(query7)
total_items = 0
count = 0
for row in result:
    total_items += row[3]
    count += 1
print(f"On average, each character that has a weapon has {(total_items/count):.2f} weapons.")
print('-'*40)

cursor.close()
connection.close()

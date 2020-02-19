import os
import pymongo
from dotenv import load_dotenv

load_dotenv()

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASS = os.getenv("MONGO_PASS")
MONGO_SERVER = os.getenv("MONGO_SERVER")

client = pymongo.MongoClient(f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_SERVER}/test?retryWrites=true&w=majority")
print("CLIENT:", type(client))
#print(dir(client))

print('-'*40)

db = client.test_database
print("DB:", type(db))
#print(dir(db))

print('-'*40)

print("COLLECTIONS:")
print(db.list_collection_names())

print('-'*40)

collection = db.pokemon
print("COLLECTION:", type(collection), collection)


collection.insert_one({
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000,
    "hp": 400
})

print('-'*40)

print("SELECT ALL PIKACHUS:")
print(collection.count_documents({}))
print(collection.count_documents({"name": "Pikachu"}))

import pymongo
import os
import json

mclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = mclient["CardGameDatabase"]

# Function to rebuild the database from the beginning 
def build_card_meta_database():
    print("Building Database...")
    collection = db["CardMeta"]
    for i in os.listdir():
        collection.insert_one(json.loads(i))

def get_card_meta():
    return db["CardMeta"]

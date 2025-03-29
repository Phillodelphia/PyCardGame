import pymongo
from bson import json_util
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
    print("Card meta has successfully been built")

# Function to create a new player
def create_new_player(name):
    player_meta = {
        "name": name,
        "player_inventory": [],
    }
    collection = db["PlayerDatabase"]

    collection.insert_one(player_meta)
    print("New player added to game")

# Function to get all available cards
def get_card_meta():
    return json_util.loads(db["CardMeta"])

# Card class that will be used for each card metadata
import rarity_types
import pymongo

class Card():
    def __init__(self, name, rarity, img="DEFAULT"):
        self.name = name
        self.rarity = rarity
        self.img = img
    
    def get_name(self) -> str:
        return self.name
    
    def get_rarity(self) -> str:
        return self.rarity
    
    def get_image(self):
        return self.img

def build_database():
    mclient = pymongo.MongoClient("mongodb://localhost:27017/")
    if "carddatabase" not in mclient.list_database_names():
        db = mclient["carddatabase"]
    
    
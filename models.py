from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
#client = MongoClient("mongodb://localhost:27017/")
client = MongoClient(os.getenv("MONGO_URI"))
db = client['typingtestdb']

users_collection = db['users']
scores_collection = db['scores']
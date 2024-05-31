import ast
from pymongo import MongoClient
from Config import MONGO_URI

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db_name = MONGO_URI.split('/')[-1]
db = client[db_name]
users_collection = db["users"]

# Users class is replaced with dictionary-based approach

async def num_users():
    return users_collection.count_documents({})

async def add_channel(user_id, channel_id):
    user = users_collection.find_one({"user_id": user_id})
    if user:
        if user.get("channels"):
            channels = list(set(ast.literal_eval(user["channels"])))
            if channel_id not in channels:
                channels.append(channel_id)
                users_collection.update_one({"user_id": user_id}, {"$set": {"channels": str(channels)}})
        else:
            users_collection.update_one({"user_id": user_id}, {"$set": {"channels": str([channel_id])}})
    else:
        user_doc = {
            "user_id": user_id,
            "channels": str([channel_id])
        }
        users_collection.insert_one(user_doc)

async def remove_channel(user_id, channel_id):
    user = users_collection.find_one({"user_id": user_id})
    if user:
        channels = list(set(ast.literal_eval(user["channels"])))
        if user.get("channels") and channel_id in channels:
            channels.remove(channel_id)
            if len(channels) == 0:
                users_collection.update_one({"user_id": user_id}, {"$set": {"channels": None}})
            else:
                users_collection.update_one({"user_id": user_id}, {"$set": {"channels": str(channels)}})
    else:
        user_doc = {
            "user_id": user_id,
            "channels": None
        }
        users_collection.insert_one(user_doc)

async def get_channels(user_id):
    user = users_collection.find_one({"user_id": user_id})
    if user:
        if user.get("channels"):
            channels = ast.literal_eval(user["channels"])
            return True, channels
        else:
            return False, []
    else:
        user_doc = {
            "user_id": user_id,
            "channels": None
        }
        users_collection.insert_one(user_doc)
        return False, []


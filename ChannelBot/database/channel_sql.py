from pymongo import MongoClient
from bson.objectid import ObjectId
from Config import MONGO_URI

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db_name = MONGO_URI.split('/')[-1]
db = client[db_name]
channels_collection = db["channels"]

# Channel class replaced with dictionary-based approach

async def num_channels():
    return channels_collection.count_documents({})

async def add_channel(channel_id, user_id):
    if not channels_collection.find_one({"channel_id": channel_id}):
        channel = {
            "channel_id": channel_id,
            "admin_id": user_id,
            "caption": None,
            "buttons": None,
            "position": None,
            "sticker_id": None,
            "edit_mode": None,
            "webpage_preview": False
        }
        channels_collection.insert_one(channel)

async def remove_channel(channel_id):
    channels_collection.delete_one({"channel_id": channel_id})

async def get_channel_info(channel_id):
    q = channels_collection.find_one({"channel_id": channel_id})
    if q:
        info = {
            'admin_id': q.get('admin_id'),
            'buttons': q.get('buttons'),
            'caption': q.get('caption'),
            'position': q.get('position'),
            'sticker_id': q.get('sticker_id'),
            'webpage_preview': q.get('webpage_preview'),
            'edit_mode': q.get('edit_mode')
        }
        return True, info
    else:
        return False, {}

async def set_caption(channel_id, caption):
    result = channels_collection.update_one({"channel_id": channel_id}, {"$set": {"caption": caption}})
    return result.modified_count > 0

async def get_caption(channel_id):
    q = channels_collection.find_one({"channel_id": channel_id}, {"caption": 1})
    if q:
        return q.get("caption", "")
    else:
        return ''

async def set_buttons(channel_id, buttons):
    result = channels_collection.update_one({"channel_id": channel_id}, {"$set": {"buttons": buttons}})
    return result.modified_count > 0

async def get_buttons(channel_id):
    q = channels_collection.find_one({"channel_id": channel_id}, {"buttons": 1})
    if q:
        return q.get("buttons")
    else:
        return None

async def set_position(channel_id, position):
    result = channels_collection.update_one({"channel_id": channel_id}, {"$set": {"position": position}})
    return result.modified_count > 0

async def get_position(channel_id):
    q = channels_collection.find_one({"channel_id": channel_id}, {"position": 1})
    if q:
        return q.get("position", "below")
    else:
        return 'below'

async def set_sticker(channel_id, sticker):
    result = channels_collection.update_one({"channel_id": channel_id}, {"$set": {"sticker_id": sticker}})
    return result.modified_count > 0

async def get_sticker(channel_id):
    q = channels_collection.find_one({"channel_id": channel_id}, {"sticker_id": 1})
    if q:
        return q.get("sticker_id")
    else:
        return None

async def toggle_webpage_preview(channel_id, value):
    result = channels_collection.update_one({"channel_id": channel_id}, {"$set": {"webpage_preview": value}})
    return result.modified_count > 0

async def get_webpage_preview(channel_id):
    q = channels_collection.find_one({"channel_id": channel_id}, {"webpage_preview": 1})
    if q:
        return q.get("webpage_preview", False)
    else:
        return False

async def set_edit_mode(channel_id, edit_mode):
    result = channels_collection.update_one({"channel_id": channel_id}, {"$set": {"edit_mode": edit_mode}})
    return result.modified_count > 0

async def get_edit_mode(channel_id):
    q = channels_collection.find_one({"channel_id": channel_id}, {"edit_mode": 1})
    if q:
        return q.get("edit_mode", "media")
    else:
        return 'media'

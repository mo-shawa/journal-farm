from model import JournalEntry
import motor.motor_asyncio
import os

client = motor.motor_asyncio.AsyncIOMotorClient(
    os.environ.get('MONGO_URL', 'none'))

database = client.JournalAI

collection = database.entries


async def fetch_entry(id):
    doc = await collection.find_one({'id': id}, {'_id': False})
    return doc


async def fetch_all_entries():
    # two ways to do this:
    # 1. cursor and loop through
    entries = []
    cursor = collection.find({})
    async for doc in cursor:
        entries.append(JournalEntry(**doc))
    return entries

    # 2. find.to_list()
    # return await collection.find().to_list(None)


async def create_entry(entry):
    document = entry
    result = await collection.insert_one(document)
    return result

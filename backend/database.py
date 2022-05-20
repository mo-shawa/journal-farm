from model import JournalEntry
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://127.0.0.1:27017/')

database = client.JournalAI

collection = database.entries


async def fetch_entry(title):
    doc = await collection.find_one({'title': title}, {'_id': False})
    return doc


async def fetch_all_entries():
    # two ways to do this:
    # 1. cursor and loop through
    entries = []
    cursor = collection.find({})
    async for doc in cursor:
        entries.append(JournalEntry(**doc))

    # 2. find.to_list()
    # return await collection.find().to_list(None)


async def create_entry(entry):
    document = entry
    await collection.insert_one(document)
    return document

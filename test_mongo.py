import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

try:
    client = MongoClient(MONGO_URL)

    # connection test
    client.admin.command("ping")

    print("MongoDB Connected Successfully ✅")

except Exception as e:
    print("Connection Failed ❌")
    print(e)
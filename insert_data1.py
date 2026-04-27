import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL_KEY = os.getenv("MONGO_DB_URL")

client = MongoClient(MONGO_URL_KEY)
db = client["customer_db"]
print("INSERT DB NAME:", db.name)

# 👉 NEW COLLECTION (marketing ke liye)
collection = db["marketing_data"]

# 👉 CSV load karo
df = pd.read_csv("notebooks/marketing_campaign.csv", delimiter="\t")
print("SHAPE:", df.shape)
print(df.head())
print(df.columns.tolist())

# 👉 Convert to dict
data = df.to_dict(orient="records")

# 👉 Insert
collection.delete_many({})  
print("Deleted old records")
print("Count after delete:", collection.count_documents({}))
collection.insert_many(data)
print("Count after insert:", collection.count_documents({}))
print(collection.find_one())

print("Marketing Data Inserted Successfully 🚀")
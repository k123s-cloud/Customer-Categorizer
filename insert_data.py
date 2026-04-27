import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL_KEY = os.getenv("MONGO_URL_KEY")

client = MongoClient(MONGO_URL_KEY)
db = client["customer_db"]
collection = db["customers"]

df = pd.read_csv(r"C:\Users\91941\Desktop\project customer categorizer\Customer-Categorizer\notebooks\data\clustered_data.csv")
print(df.head())

data = df.to_dict(orient="records")

collection.insert_many(data)

print("Data Inserted Successfully 🚀")
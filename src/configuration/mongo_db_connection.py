"""import os
import pymongo
import certifi
import pandas as pd

#from src.constant.database import DATABASE_NAME
#from src.constant.env_variable import MONGODB_URL_KEY
#from src.exception import CustomerException

ca = certifi.where()


class MongoDBClient:
    #client = None

    def __init__(self, database_name="ineuron", collection_name="customer_sementation"):
        try:
            #if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                #MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            #self.client = MongoDBClient.client
            self.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.database = self.client[database_name]
            #self.database_name = database_name
            self.collection = self.database[collection_name]
            print("Connected to MongoDB successfully")
            self.collection.delete_many({})  # Clear the collection before inserting new data
            print("Deleted exixting data from MONGODB")
            df = pd.read_csv(r"notebook\marketing_campaign.csv", delimiter="\t")
            df.columns = df.columns.str.strip()  # Remove leading/trailing whitespace from column names
            df = df.astype(str)
            data = df.to_dict(orient="records")
            self.collection.insert_many(data)
            print(f" Successfully uploaded {len(data)} records to MONGODB!")
            sample_data = list(self.collection.find({}, {"_id": 0}).limit(5))
            print("Sample data from MONGODB:")
            for record in sample_data:
                print(record)
        except Exception as e:
            raise Exception(f"MONGODB connection failed: {e}")"""
            

import os
import pymongo
import certifi
from dotenv import load_dotenv

load_dotenv()

ca = certifi.where()


class MongoDBClient:
    client = None

    def __init__(self, database_name="customer_db", collection_name="marketing_data"):
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv("MONGO_DB_URL")

                if mongo_db_url is None:
                    raise Exception("Environment key MONGO_DB_URL is not set.")

                MongoDBClient.client = pymongo.MongoClient(
                    mongo_db_url,
                    tlsCAFile=ca
                )

            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.collection = self.database[collection_name]

            print("Connected to MongoDB successfully")

        except Exception as e:
            raise Exception(f"MongoDB connection failed: {e}")

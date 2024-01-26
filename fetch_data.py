import requests
from pymongo import MongoClient
import json

# MongoDB connection settings
mongo_uri = "mongodb://mongodb:27017/"  # Update with your MongoDB URI
mongo_db_name = "your_db_name"          # Update with your database name
mongo_collection_name = "your_collection_name"  # Update with your collection name

# URL to fetch data from
url = "https://gdmf.apple.com/v2/pmv"

# Establish MongoDB connection
mongo_client = MongoClient(mongo_uri)
mongo_db = mongo_client[mongo_db_name]
mongo_collection = mongo_db[mongo_collection_name]

# Fetch data from URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON data
    data = response.json()

    # Insert data into MongoDB
    # You might need to adjust this if data is a list or nested structure
    mongo_collection.insert_one(data)

    print("Data inserted into MongoDB.")
else:
    print("Failed to fetch data. Status code:", response.status_code)

# Close MongoDB connection
mongo_client.close()

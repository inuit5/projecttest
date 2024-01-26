import pandas as pd
import mysql.connector
from pymongo import MongoClient

# MongoDB connection settings
mongo_uri = "mongodb://mongodb:27017/"
mongo_db_name = "your_db_name"
mongo_collection_name = "your_collection_name"

# MySQL connection settings
mysql_config = {
    'user': 'root',
    'password': 'password',
    'host': 'mysql',
    'database': 'data_db',
    'raise_on_warnings': True
}

# Connect to MongoDB
mongo_client = MongoClient(mongo_uri)
mongo_db = mongo_client[mongo_db_name]
mongo_collection = mongo_db[mongo_collection_name]

# Fetch data from MongoDB
mongo_docs = list(mongo_collection.find({}))

# Convert to Pandas DataFrame
df = pd.DataFrame(mongo_docs)

# Connect to MySQL
mysql_conn = mysql.connector.connect(**mysql_config)
cursor = mysql_conn.cursor()

# Prepare a SQL query to insert data
# Note: Adjust the SQL statement according to your table schema
insert_sql = """
INSERT INTO your_table_name (column1, column2, ...)
VALUES (%s, %s, ...)
"""
# Iterate over DataFrame rows and execute SQL query for each row
for row in df.itertuples(index=False):
    cursor.execute(insert_sql, tuple(row))

# Commit and close MySQL connection
mysql_conn.commit()
cursor.close()
mysql_conn.close()

print("Data transfer complete.")

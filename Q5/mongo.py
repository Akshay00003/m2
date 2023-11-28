import pymongo

# Connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string

# Specify the database and collection
db = client["your_database_name"]  # Replace with your database name
collection = db["your_collection_name"]  # Replace with your collection name


# Data to be inserted (replace with your data)
data_to_insert = {
    "name": "sue",
    "age": 26,
    "groups": ["mews", "sports"]
}

# Insert the document into the collection
result = collection.insert_one(data_to_insert)

# Print the inserted document's ID
print(f"Document inserted with ID: {result.inserted_id}")
print(data_to_insert)
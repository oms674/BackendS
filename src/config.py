from pymongo import MongoClient

# Connect to MongoDB
MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)

# Database and Collection
db = client["image_db"]
requests_collection = db["requests"]

# Test Connection
try:
    client.admin.command('ping')
    print("✅ Successfully connected to MongoDB!")
except Exception as e:
    print(f"❌ Error connecting to MongoDB: {e}")

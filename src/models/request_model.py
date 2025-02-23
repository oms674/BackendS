from pymongo import MongoClient
import uuid

# Connect to MongoDB
MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)
db = client["image_db"]
requests_collection = db["requests"]

def create_request(products):
    """Insert a new processing request into the database."""
    request_id = str(uuid.uuid4())
    data = {
        "request_id": request_id,
        "status": "PENDING",
        "products": products
    }
    requests_collection.insert_one(data)
    return request_id

def update_request_status(request_id, status, processed_data=None):
    """Update request status and add output image URLs."""
    update_data = {"status": status}
    if processed_data:
        update_data["products"] = processed_data

    requests_collection.update_one({"request_id": request_id}, {"$set": update_data})

def get_request_status(request_id):
    """Fetch the status of a request from MongoDB."""
    request_data = requests_collection.find_one({"request_id": request_id}, {"_id": 0})
    return request_data


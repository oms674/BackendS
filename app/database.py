from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI, HTTPException
from bson import ObjectId

app = FastAPI()

# MongoDB connection details
MONGO_URI = "mongodb://localhost:27017"  # Update with your MongoDB URI if needed
DATABASE_NAME = "image_db"

# Establish MongoDB connection
client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]

# MongoDB collections
requests_collection = db["requests"]

@app.on_event("startup")
async def startup_db():
    # Check if MongoDB is reachable by attempting a simple ping
    try:
        await client.admin.command('ping')
        print("MongoDB connected successfully!")
    except Exception as e:
        print("Error connecting to MongoDB:", e)

@app.get("/db-status")
async def check_db_status():
    try:
        # Simple ping to check connection
        await client.admin.command('ping')
        return {"status": "success", "message": "MongoDB connection is active."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {e}")

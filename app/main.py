from fastapi import FastAPI, HTTPException
from app.routes import upload, status
from app.database import client
import logging

# Initialize FastAPI app
app = FastAPI()

# Include the upload and status routes
app.include_router(upload.router, prefix="/api", tags=["Upload"])
app.include_router(status.router, prefix="/api", tags=["Status"])

# MongoDB connection check
@app.on_event("startup")
async def startup_db():
    try:
        # Check MongoDB connection during FastAPI app startup
        await client.admin.command('ping')
        print("MongoDB connected successfully!")
    except Exception as e:
        logging.error(f"Error connecting to MongoDB: {e}")
        raise HTTPException(status_code=500, detail="Database connection error")

# Root endpoint for checking if the API is live
@app.get("/")
async def read_root():
    return {"message": "FastAPI app is running!"}

# Optional: Add a /health endpoint to check the API health status
@app.get("/health")
async def health_check():
    return {"status": "API is healthy!"}

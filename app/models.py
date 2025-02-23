from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

# This class is used for data validation when creating/updating requests
class ImageProcessingRequest(BaseModel):
    request_id: str
    status: str  # e.g., 'pending', 'processing', 'completed', 'failed'
    output_csv: Optional[str] = None  # Path to the output CSV (could be None initially)

    class Config:
        # This allows Pydantic to work with MongoDB's ObjectId, converting it to string for JSON responses
        json_encoders = {ObjectId: str}

# The following is a MongoDB document model (not used directly with FastAPI)
# but it can be useful for understanding what will be stored in the database.
class MongoImageProcessingRequest:
    def __init__(self, request_id: str, status: str, output_csv: Optional[str] = None):
        self.request_id = request_id
        self.status = status
        self.output_csv = output_csv

from pydantic import BaseModel
from typing import Optional
from uuid import UUID

# Schema to be used when returning data from the API
class ImageProcessingRequestResponse(BaseModel):
    request_id: UUID
    status: str  # e.g., 'pending', 'processing', 'completed', 'failed'
    output_csv: Optional[str] = None  # URL or path to the output CSV after processing

    class Config:
        # This tells Pydantic to handle UUIDs correctly in JSON responses
        json_encoders = {UUID: str}


# Schema for the input when uploading the CSV (you may not need much here as the actual file is handled by FastAPI)
class CSVUploadRequest(BaseModel):
    file: str  # This is a placeholder for file upload
    # If you need any extra data in the request (e.g., a title), you can add fields here.
    # For example: title: Optional[str] = None

# Schema to be used for the status response
class StatusResponse(BaseModel):
    request_id: UUID
    status: str
    output_csv: Optional[str] = None  # Path or URL of the processed output CSV

    class Config:
        json_encoders = {UUID: str}

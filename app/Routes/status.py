from fastapi import APIRouter, File, UploadFile, HTTPException
from app.schemas import CSVUploadRequest
from app.database import requests_collection
from app.worker import process_images
import uuid

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Generate unique request_id for this processing job
    request_id = str(uuid.uuid4())

    # Here we would handle the CSV file (save it, validate, etc.)
    # For now, let's assume the file is validated and ready for processing

    # Insert the request into the MongoDB collection
    await requests_collection.insert_one({
        "request_id": request_id,
        "status": "pending",
        "output_csv": None
    })

    # Process the images asynchronously using Celery
    process_images.delay(request_id, ["image_url_1", "image_url_2"])

    return {"request_id": request_id}

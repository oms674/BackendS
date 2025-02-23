from fastapi import APIRouter, HTTPException  # Import HTTPException here
from app.database import requests_collection
from app.schemas import StatusResponse

router = APIRouter()

@router.get("/status/{request_id}", response_model=StatusResponse)
async def check_status(request_id: str):
    # Retrieve the document from the MongoDB collection
    request = await requests_collection.find_one({"request_id": request_id})

    if not request:
        # Raise an HTTPException if the request is not found
        raise HTTPException(status_code=404, detail="Request not found")

    return StatusResponse(
        request_id=request["request_id"],
        status=request["status"],
        output_csv=request.get("output_csv")
    )

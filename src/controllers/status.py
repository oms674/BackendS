from fastapi import APIRouter, HTTPException
from src.models.request_model import get_request_status

router = APIRouter()

@router.get("/status/{request_id}")
async def get_status(request_id: str):
    """API to check the processing status of a request."""
    request_data = get_request_status(request_id)
    
    if not request_data:
        raise HTTPException(status_code=404, detail="Request ID not found")

    return request_data

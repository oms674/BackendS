from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks
from src.utils.csv_parser import parse_csv
from src.models.request_model import create_request
from src.services.process_images import process_images

router = APIRouter()

@router.post("/upload")
async def upload_csv(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    """API to accept and process CSV uploads asynchronously."""
    try:
        products = parse_csv(file)
        request_id = create_request(products)

        # Run image processing in a background thread
        background_tasks.add_task(process_images, request_id, products)

        return {"request_id": request_id, "status": "Processing started"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

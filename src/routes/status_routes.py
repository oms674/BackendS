from fastapi import APIRouter
from src.controllers.status import router as status_router

router = APIRouter()
router.include_router(status_router, prefix="/api")

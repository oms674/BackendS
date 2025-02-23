from fastapi import FastAPI
from src.routes.upload_routes import router as upload_routes
from src.routes.status_routes import router as status_routes
from src.config import db  # Ensure MongoDB connection

app = FastAPI()

app.include_router(upload_routes)
app.include_router(status_routes)

@app.get("/")
async def root():
    return {"message": "FastAPI Image Processing Backend is Running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

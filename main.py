from fastapi import FastAPI
from database import engine
from models import Base

from auth import router as auth_router
from jobs import router as jobs_router
from apply import router as apply_router
from upload import router as upload_router

    
Base.metadata.create_all(bind=engine)

app = FastAPI(title="JobApply API")

app.include_router(auth_router)
app.include_router(jobs_router)
app.include_router(apply_router)
app.include_router(upload_router)
    
@app.get("/")
def home():
    return {"message": "JobApply API is running successfully!"}
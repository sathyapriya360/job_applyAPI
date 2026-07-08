from fastapi import APIRouter

router = APIRouter(
    prefix="/apply",
    tags=["Apply"]
)

@router.post("/")
def apply_job():
    return {"message": "Job application submitted successfully"}
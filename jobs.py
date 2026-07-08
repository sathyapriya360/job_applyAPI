from fastapi import APIRouter

router = APIRouter(prefix="/jobs", tags=["Jobs"])

jobs = [
    {
        "id": 1,
        "title": "Python Developer",
        "company": "ABC Technologies",
        "location": "Chennai"
    },
    {
        "id": 2,
        "title": "Frontend Developer",
        "company": "XYZ Solutions",
        "location": "Bangalore"
    }
]

@router.get("/")
def get_jobs():
    return jobs

@router.get("/{job_id}")
def get_job(job_id: int):
    for job in jobs:
        if job["id"] == job_id:
            return job
    return {"message": "Job not found"}
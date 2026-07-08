# JobApply API

A RESTful Job Application Automation API built using **FastAPI** and **SQLite**. This project allows users to register, view jobs, apply for jobs, and upload resumes through REST APIs with interactive Swagger documentation.

---

## Features

- User Registration API
- Job Listing API
- Job Application API
- Resume Upload API
- SQLite Database
- FastAPI Backend
- Swagger UI Documentation

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn
- Pydantic

---

## Project Structure

```
jobapply-api/
│── main.py
│── database.py
│── models.py
│── schemas.py
│── auth.py
│── jobs.py
│── apply.py
│── upload.py
│── requirements.txt
│── README.md
│── jobapply.db
│── uploads/
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/sathyapriya360/jobapply-api.git
cd jobapply-api
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python -m uvicorn main:app --reload
```

The API will start at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Home

```
GET /
```

Returns the API status.

### User Registration

```
POST /auth/register
```

Registers a new user.

### Jobs

```
GET /jobs/
```

Returns all available jobs.

```
GET /jobs/{job_id}
```

Returns details of a specific job.

### Apply

```
POST /apply/
```

Applies for a job.

### Resume Upload

```
POST /upload/resume
```

Uploads a PDF resume.

---

## Database

- SQLite
- Database File: `jobapply.db`

---

## Future Improvements

- User Login
- JWT Authentication
- Password Hashing
- Search Jobs API
- Store Job Applications in Database
- Email Notifications

---

## Author

**Sathyapriya V**

B.E. Computer Science and Engineering (AI & ML)

---

## License

This project is developed for educational and internship purposes.
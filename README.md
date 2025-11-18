# To-Do REST API

A simple **To-Do REST API** built with **FastAPI**, **SQLAlchemy**, and **JWT authentication**.

---

## Features

- User registration & login with JWT
- CRUD operations for tasks
- Each user can only access their tasks
- Swagger UI API docs
- SQLite (default) / PostgreSQL support
- Unit tests with pytest

---

## Tech Stack

- **Backend**: FastAPI
- **Database**: SQLAlchemy + SQLite / PostgreSQL
- **Authentication**: JWT
- **Testing**: pytest
- **Documentation**: OpenAPI / Swagger

---

## Installation

```bash
# Clone repo
git clone <repo_url>
cd todo_api

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate 

# Install dependencies
pip install -r requirements.txt

# Run app
uvicorn main:app --reload
```

## API Endpoints

- Register: POST /api/v1/auth/register
- Login: POST /api/v1/auth/login
- Tasks CRUD: GET/POST/PATCH/DELETE /api/v1/tasks

- Swagger UI available at: http://127.0.0.1:8000/docs
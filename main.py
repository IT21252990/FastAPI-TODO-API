from fastapi import FastAPI
from app.core.config import settings
from app.database import Base, engine

# Routers
from app.auth.routes import router as auth_router
from app.tasks.routes import router as tasks_router


# Initialize FastAPI app
app = FastAPI(title=settings.APP_NAME)

# Include Routers
app.include_router(auth_router, prefix=settings.API_V1_STR)
app.include_router(tasks_router, prefix=settings.API_V1_STR)

# Create tables on startup (DEV only)
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the To-Do REST API!"}

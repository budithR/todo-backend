from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models.todo import Base
from app.routers.todo import router as todo_router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simple Todo API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todo_router)

@app.get("/")
def root():
    return {"message": "Todo API is working! Visit /docs for Swagger UI"}
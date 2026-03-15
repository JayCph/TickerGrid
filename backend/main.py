import models
from database import Base, engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

_ = models.Ticker

# Create the database file
Base.metadata.create_all(bind=engine)

app = FastAPI(title="TickerGrid API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    return {
        "status": "online",
        "message": "TickerGrid API is live and database is connected!",
    }

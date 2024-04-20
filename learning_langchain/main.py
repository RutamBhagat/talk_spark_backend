from fastapi import FastAPI
from routers import summarizer
from dotenv import load_dotenv


load_dotenv()

app = FastAPI()


app.include_router(
    summarizer.router,
    prefix="/summarizer",
    tags=["summarizer"],
)

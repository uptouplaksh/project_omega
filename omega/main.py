from fastapi import FastAPI
from omega.api import events
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Project Omega",
    description="Cyber Decision Intelligence System",
    version="0.1.0",
)

app.include_router(events.router)


@app.get("/health")
async def health():
    return{"status":"omega-online"}


@app.get("/")
async def root():
    return{"message":"Project OMEGA API is running"}
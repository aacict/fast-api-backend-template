from fastapi import FastAPI
from app.core.logging import setup_logging
from prometheus_fastapi_instrumentator import Instrumentator
import logging

setup_logging()

logger = logging.getLogger(__name__)

app = FastAPI()

#Initializing the prometheus instrumentator
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

@app.get("/")
async def root():
    logger.info("Root endpoint called....")
    return {"message": "Hello with FastAPI and Prometheus!"}

@app.get("/health")
async def health_check():
    logger.info("Health check endpoint called....")
    return {"status": "ok"}
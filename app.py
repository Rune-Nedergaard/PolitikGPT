"""
Danish Statistics Explorer - Main Application

This is the main entry point for the Danish Statistics Explorer application.
It initializes the backend server and handles API requests from the frontend.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Import configuration
try:
    from config import DEBUG_MODE
except ImportError:
    logger.error("Configuration module not found. Please ensure config.py exists.")
    DEBUG_MODE = False

# Create FastAPI app
app = FastAPI(
    title="Danish Statistics Explorer",
    description="Access Danish statistics through an intelligent, conversational interface",
    version="0.1.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define API models
class Query(BaseModel):
    text: str
    language: str = "en"
    session_id: str = None

class QueryResponse(BaseModel):
    response: str
    visualizations: list = []
    suggested_followups: list = []

# Define API endpoints
@app.get("/")
async def read_root():
    return {"message": "Danish Statistics Explorer API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/query", response_model=QueryResponse)
async def process_query(query: Query):
    """
    Process a user query about Danish statistics
    """
    try:
        # Placeholder response until agent implementation
        return QueryResponse(
            response="This is a placeholder response. Query processing not yet implemented.",
            visualizations=[],
            suggested_followups=["What is the population of Denmark?", "How has unemployment changed in the last decade?"]
        )
    except Exception as e:
        logger.error(f"Error processing query: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Serve static files for frontend
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# Run the application
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=DEBUG_MODE) 
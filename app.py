"""
Main application file for the Danish Statistics Explorer.

This module initializes the FastAPI application and defines the core routes
for frontend-backend communication.
"""
import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
from pydantic import BaseModel
from typing import List, Optional, Dict, Any

# Import configuration
import config

# Set up logging
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Danish Statistics Explorer API",
    description="Backend API for the Danish Statistics Explorer application",
    version="0.1.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define API models
class QueryRequest(BaseModel):
    query: str
    language: str = "en"
    conversation_id: Optional[str] = None
    context: Optional[Dict[str, Any]] = None

class QueryResponse(BaseModel):
    response: str
    visualizations: Optional[List[Dict[str, Any]]] = None
    data_table: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None

@app.get("/")
async def root():
    """Health check endpoint."""
    return {"status": "ok", "message": "Danish Statistics Explorer API is running"}

@app.post("/api/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    """
    Process a natural language query about Danish statistics.
    
    This endpoint takes a user query, analyzes it using the Gemini Flash 2.0 model,
    retrieves relevant data from the Statistics Denmark API, and returns a response
    with optional visualizations and data tables.
    """
    try:
        logger.info(f"Received query: {request.query}")
        
        # Placeholder for actual implementation
        # TODO: Implement query processing pipeline with agents
        
        return QueryResponse(
            response="This is a placeholder response. The full implementation will process your query about Danish statistics.",
            visualizations=[],
            data_table=None,
            metadata={"processed": True, "query_understood": True}
        )
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler for all unhandled exceptions."""
    logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred. Please try again later."},
    )

if __name__ == "__main__":
    logger.info("Starting Danish Statistics Explorer API")
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=config.DEBUG) 
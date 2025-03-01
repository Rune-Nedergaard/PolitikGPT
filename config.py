"""
Configuration management for the Danish Statistics Explorer application.

This module centralizes configuration handling, including environment variables,
API keys, and application settings.
"""
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

# Base paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
CACHE_DIR = BASE_DIR / "cache"

# Ensure required directories exist
DATA_DIR.mkdir(exist_ok=True)
CACHE_DIR.mkdir(exist_ok=True)

# API Configuration
API_BASE_URL = "https://api.statbank.dk/v1"
API_TIMEOUT = int(os.getenv("API_TIMEOUT", "30"))

# Gemini Flash API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash-2.0-latest")

# Language settings
DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "en")  # 'en' or 'da'
SUPPORTED_LANGUAGES = ["en", "da"]

# Application settings
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
MAX_CACHE_SIZE_MB = int(os.getenv("MAX_CACHE_SIZE_MB", "500"))

# Check for required environment variables
if not GEMINI_API_KEY:
    raise EnvironmentError("GEMINI_API_KEY is required but not set") 
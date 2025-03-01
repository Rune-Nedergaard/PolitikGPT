"""
Configuration settings for the Danish Statistics Explorer application.

This module loads environment variables and provides configuration settings
for the application, including API keys, endpoints, and application settings.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
STATBANK_API_BASE_URL = "https://api.statbank.dk/v1"

# Application Configuration
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"
DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "en")  # Default to English
CACHE_EXPIRY = int(os.getenv("CACHE_EXPIRY", "3600"))  # Default 1 hour (in seconds)

# Gemini Model Configuration
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash-latest")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.2"))
TOP_P = float(os.getenv("TOP_P", "0.95"))
MAX_OUTPUT_TOKENS = int(os.getenv("MAX_OUTPUT_TOKENS", "8192"))

# Application paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
CACHE_DIR = os.path.join(DATA_DIR, "cache")

# Ensure required directories exist
os.makedirs(CACHE_DIR, exist_ok=True)

# Validate required environment variables
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set")

# Export configuration variables
__all__ = [
    "GEMINI_API_KEY",
    "STATBANK_API_BASE_URL",
    "DEBUG_MODE",
    "DEFAULT_LANGUAGE",
    "CACHE_EXPIRY",
    "GEMINI_MODEL",
    "TEMPERATURE",
    "TOP_P",
    "MAX_OUTPUT_TOKENS",
    "BASE_DIR",
    "DATA_DIR",
    "CACHE_DIR",
] 
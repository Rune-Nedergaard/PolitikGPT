import os
import logging
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_config():
    """
    Load environment variables and configuration settings.
    
    Returns:
        dict: Dictionary containing configuration settings
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Configuration dictionary
    config = {
        # API settings
        "statbank_api_url": "https://api.statbank.dk/v1",
        
        # Gemini API settings
        "gemini_endpoint": os.getenv("GEMINI_ENDPOINT"),
        "gemini_key": os.getenv("GEMINI_KEY"),
        "gemini_deployment": os.getenv("GEMINI_DEPLOYMENT"),
        
        # Application settings
        "debug_mode": os.getenv("DEBUG_MODE", "False").lower() in ("true", "1", "t"),
        "cache_ttl": int(os.getenv("CACHE_TTL", "3600")),  # Cache time-to-live in seconds
        
        # Language settings
        "default_language": os.getenv("DEFAULT_LANGUAGE", "da"),
    }
    
    # Validate critical configuration
    validate_config(config)
    
    return config

def validate_config(config):
    """
    Validate that critical configuration settings are present.
    
    Args:
        config (dict): Configuration dictionary to validate
    
    Raises:
        ValueError: If critical configuration is missing
    """
    # Check Gemini API settings
    if not all([config["gemini_endpoint"], config["gemini_key"], config["gemini_deployment"]]):
        logger.warning("Missing Gemini API configuration. LLM functionality will not work.")
    
    # Check StatBank API
    if not config["statbank_api_url"]:
        raise ValueError("Statistics Denmark API URL is required")

def get_language_config(config, language=None):
    """
    Get language-specific configuration.
    
    Args:
        config (dict): Main configuration dictionary
        language (str, optional): Language code to use. Defaults to config default.
    
    Returns:
        dict: Dictionary of language-specific settings
    """
    # Use provided language or fall back to default
    lang = language or config["default_language"]
    
    # Language-specific settings
    lang_settings = {
        "da": {
            "date_format": "%d-%m-%Y",
            "thousands_separator": ".",
            "decimal_separator": ",",
            "currency_symbol": "kr",
        },
        "en": {
            "date_format": "%Y-%m-%d",
            "thousands_separator": ",",
            "decimal_separator": ".",
            "currency_symbol": "DKK",
        }
    }
    
    # Return language settings or English as fallback
    return lang_settings.get(lang, lang_settings["en"]) 
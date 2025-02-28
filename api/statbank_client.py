import requests
import json
import logging
from typing import Dict, List, Any, Optional, Union
import pandas as pd

# Set up logging
logger = logging.getLogger(__name__)

class StatbankClient:
    """Client for interacting with Statistics Denmark's Statbanks API."""
    
    def __init__(self, base_url: str = "https://api.statbank.dk/v1"):
        """
        Initialize the StatbankClient.
        
        Args:
            base_url: The base URL for the Statbanks API
        """
        self.base_url = base_url
        
    def _make_request(self, endpoint: str, method: str = "GET", params: Optional[Dict] = None, 
                      data: Optional[Dict] = None) -> Dict:
        """
        Make an HTTP request to the Statbanks API.
        
        Args:
            endpoint: The API endpoint to call
            method: HTTP method (GET or POST)
            params: Query parameters for GET requests
            data: JSON data for POST requests
            
        Returns:
            Dict: The JSON response from the API
            
        Raises:
            Exception: If the request fails
        """
        url = f"{self.base_url}/{endpoint}"
        
        try:
            if method == "GET":
                response = requests.get(url, params=params)
            elif method == "POST":
                headers = {"Content-Type": "application/json"}
                response = requests.post(url, headers=headers, json=data)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            raise Exception(f"Failed to fetch data from Statistics Denmark API: {e}")
    
    def get_tables(self, lang: str = "da") -> List[Dict]:
        """
        Get a list of available tables.
        
        Args:
            lang: Language code ("da" for Danish, "en" for English)
            
        Returns:
            List of table metadata objects
        """
        endpoint = "tableinfo"
        params = {"lang": lang}
        return self._make_request(endpoint, params=params)
    
    def get_table_metadata(self, table_id: str, lang: str = "da") -> Dict:
        """
        Get metadata for a specific table.
        
        Args:
            table_id: The table ID
            lang: Language code
            
        Returns:
            Dict containing table metadata
        """
        endpoint = "tableinfo"
        params = {"id": table_id, "lang": lang}
        return self._make_request(endpoint, params=params)
    
    def get_variables(self, table_id: str, lang: str = "da") -> List[Dict]:
        """
        Get variables available for a specific table.
        
        Args:
            table_id: The table ID
            lang: Language code
            
        Returns:
            List of variables for the table
        """
        table_metadata = self.get_table_metadata(table_id, lang)
        return table_metadata.get("variables", [])
    
    def get_variable_values(self, table_id: str, variable_id: str, lang: str = "da") -> List[Dict]:
        """
        Get possible values for a specific variable in a table.
        
        Args:
            table_id: The table ID
            variable_id: The variable ID
            lang: Language code
            
        Returns:
            List of possible values for the variable
        """
        endpoint = "variables"
        params = {"id": f"{table_id}.{variable_id}", "lang": lang}
        response = self._make_request(endpoint, params=params)
        return response.get("values", [])
    
    def get_data(self, table_id: str, variables: Dict[str, List[str]], format_type: str = "JSONSTAT", 
                lang: str = "da") -> Union[Dict, pd.DataFrame]:
        """
        Get data from a table with specified variable values.
        
        Args:
            table_id: The table ID
            variables: Dictionary mapping variable IDs to lists of value codes
            format_type: Response format ("JSONSTAT", "CSV", etc.)
            lang: Language code
            
        Returns:
            Data response (JSON or DataFrame depending on format)
        """
        endpoint = "data"
        data = {
            "table": table_id,
            "format": format_type,
            "variables": [{"code": var_id, "values": values} for var_id, values in variables.items()],
            "lang": lang
        }
        
        response = self._make_request(endpoint, method="POST", data=data)
        
        # If requesting as CSV or similar, convert to DataFrame
        if format_type in ["CSV", "PANDAS"]:
            # Process the CSV data into a DataFrame
            # This is a simplification - actual implementation would depend on the exact format
            return pd.DataFrame(response)
        
        return response
    
    def search_tables(self, query: str, lang: str = "da") -> List[Dict]:
        """
        Search for tables matching the given query.
        
        Args:
            query: Search query string
            lang: Language code
            
        Returns:
            List of matching tables
        """
        endpoint = "tableinfo"
        params = {"search": query, "lang": lang}
        return self._make_request(endpoint, params=params)
    
    def get_subjects(self, lang: str = "da") -> List[Dict]:
        """
        Get the subject hierarchy of tables.
        
        Args:
            lang: Language code
            
        Returns:
            List of subjects
        """
        endpoint = "subjects"
        params = {"lang": lang}
        return self._make_request(endpoint, params=params)

# Helper functions to work with the client

def find_relevant_tables(client: StatbankClient, query: str, lang: str = "da", 
                         max_results: int = 5) -> List[Dict]:
    """
    Find tables that might be relevant to a natural language query.
    
    Args:
        client: StatbankClient instance
        query: Natural language query
        lang: Language code
        max_results: Maximum number of tables to return
        
    Returns:
        List of relevant tables
    """
    # For now, just search directly
    # In a more advanced implementation, we could use NLP to extract keywords
    tables = client.search_tables(query, lang)
    
    # Sort by relevance and limit results
    # (Assuming the API returns tables in order of relevance)
    return tables[:max_results]

def extract_variables_from_table(client: StatbankClient, table_id: str, 
                                lang: str = "da") -> Dict[str, List[Dict]]:
    """
    Extract all variables and their possible values from a table.
    
    Args:
        client: StatbankClient instance
        table_id: The table ID
        lang: Language code
        
    Returns:
        Dictionary mapping variable IDs to lists of possible values
    """
    variables = client.get_variables(table_id, lang)
    result = {}
    
    for variable in variables:
        var_id = variable.get("id")
        var_values = client.get_variable_values(table_id, var_id, lang)
        result[var_id] = var_values
    
    return result 
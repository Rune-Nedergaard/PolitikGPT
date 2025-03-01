# Danish Statistics Explorer

A public web application providing non-technical users with easy access to Statistics Denmark's Statbanks API through an intelligent, conversational interface.

## Project Overview

The Danish Statistics Explorer bridges the gap between complex statistical data and everyday users by leveraging Gemini Flash 2.0 within an intuitive interface. The system uses DSPy as an agentic framework to intelligently identify user needs, suggest appropriate datasets, perform multi-hop reasoning when necessary, and present results through clean, minimalist visualizations.

## Features

- Conversational interface for querying Danish statistical data
- Intelligent dataset suggestion based on user queries
- Clean, minimalist visualizations of complex statistical data
- Multi-hop reasoning for complex queries
- Bilingual support (Danish and English)
- No coding knowledge required

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Gemini Flash 2.0 API key

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/Rune-Nedergaard/danish-data-dialogue.git
   cd danish-data-dialogue
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file based on `.env.example` and add your Gemini Flash 2.0 API key:
   ```
   cp .env.example .env
   # Edit .env file to add your API key
   ```

4. Run the application:
   ```
   python app.py
   ```

## Project Structure

- `agents/`: DSPy agents for query understanding and processing
- `api/`: Statistics Denmark API client
- `data/`: Data processing and metadata management
- `utils/`: Utility functions
- `frontend/`: UI components and styling
- `visualizations/`: Data visualization components
- `tests/`: Testing modules

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
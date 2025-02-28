# Statistics Denmark Data Explorer

An intelligent, conversational interface for exploring Statistics Denmark's Statbanks API. This application provides non-technical users with easy access to Danish statistical data through natural language queries and interactive visualizations.

## Features

- Natural language query processing for Statistics Denmark data
- Automatic visualization generation based on data context
- Interactive data exploration with follow-up questions
- Bilingual support (Danish and English)
- Data and visualization export capabilities

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Azure OpenAI API access (for natural language processing)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/statbank-explorer.git
   cd statbank-explorer
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file based on `.env.example` and add your API keys:
   ```
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. Run the application:
   ```
   streamlit run app.py
   ```

## Usage

Simply enter questions about Danish statistics in the chat interface. For example:

- "What's the population of Denmark?"
- "Show me unemployment rates over the last 5 years"
- "Compare GDP growth across different regions"

The application will find relevant data, generate appropriate visualizations, and provide insights based on your queries.

## Development

This project is under active development. See the project-steps.md file for the implementation roadmap.

## License

[Your chosen license] 
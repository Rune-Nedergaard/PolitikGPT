# Danish Statistics Explorer

A public web application that provides non-technical users with easy access to Statistics Denmark's Statbanks API through an intelligent, conversational interface.

## Overview

The Danish Statistics Explorer bridges the gap between complex statistical data and everyday users by leveraging Gemini Flash 2.0 within an intuitive interface. The application guides users through an exploratory research process, helping them discover, analyze, and visualize Danish statistical data without requiring any coding knowledge.

## Features

- Intelligent identification of user needs through natural language queries
- Suggestions of appropriate datasets based on user questions
- Multi-hop reasoning for complex statistical inquiries
- Clean, minimalist visualizations of Danish statistical data
- Bilingual support (Danish and English)

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Node.js 18 or higher
- Gemini Flash 2.0 API key

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/Rune-Nedergaard/danish-data-dialogue.git
   cd danish-data-dialogue
   ```

2. Install backend dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Install frontend dependencies:
   ```
   cd frontend
   npm install
   cd ..
   ```

4. Create a `.env` file based on `.env.example` and add your Gemini Flash 2.0 API key.

5. Run the development server:
   ```
   python app.py
   ```

6. In a separate terminal, start the frontend:
   ```
   cd frontend
   npm run dev
   ```

7. Access the application at http://localhost:5173

## Target Audience

- Non-technical users interested in accessing and analyzing Danish statistics
- Researchers, journalists, students, and citizens seeking insights from public data
- Anyone who wants to explore Danish statistical data without programming expertise

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
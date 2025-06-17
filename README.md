# AI Assistant App with Streamlit and OpenAI

This project implements a simple AI assistant using Streamlit for the frontend and OpenAI's GPT-4 for the backend. Users can ask questions and receive AI-generated responses through a clean web interface.

## Features

- Clean and simple web interface using Streamlit
- Powered by OpenAI's GPT-4 model
- Real-time question answering
- Secure API key management using environment variables

## Prerequisites

- Python 3.x
- OpenAI API key
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd my_ai_assistant
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

1. Make sure your virtual environment is activated
2. Run the Streamlit app:
```bash
streamlit run app.py
```
3. Open your browser and navigate to the URL shown in the terminal (typically http://localhost:8501)
4. Type your question in the text input and press Enter to get a response

## Project Structure

```
my_ai_assistant/
├── app.py              # Streamlit frontend
├── agent.py            # OpenAI integration
├── .env               # Environment variables (not tracked in git)
├── requirements.txt   # Project dependencies
└── README.md         # This file
```

## Security Note

Never commit your `.env` file or expose your OpenAI API key. The `.env` file is already included in `.gitignore` to prevent accidental commits.

## License

This project is open source and available under the MIT License. 
# Noha Chat 🤖

Noha Chat is a clean, minimal chatbot web application built using **Streamlit**, **LangChain**, and the **Google Gemini API**. It maintains conversational memory during your session, allowing you to have natural, fluid interactions with the latest AI model.

## Features

- **Conversational Memory:** Remembers context across the entire chat session.
- **Modern UI:** Built on Streamlit's native chat components for a native look and feel.
- **Up-to-Date Model:** Leverages Google's `gemini-2.5-flash` model for fast, accurate responses.
- **Secure Configuration:** Protects API keys using environmental variables.

---

## Prerequisites

Before running the application, make sure you have:
1. **Python 3.9** or higher installed.
2. A **Google Gemini API Key** (you can get one for free from Google AI Studio).

---

## Installation & Setup

Follow these steps to set up and run Noha Chat locally:

### 1. Clone or Download the Project
Save the project files into a folder on your computer.

### 2. Create a Virtual Environment (Recommended)
Open your terminal/command prompt, navigate to your project directory, and run:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
Install the required packages using pip:
```bash
pip install streamlit langchain-google-genai python-dotenv
```

### 4. Configure Your Environment Variables
Create a file named `.env` in the root directory of your project (the same folder where your Python script lives) and add your API key:
```env
GOOGLE_API_KEY=your_actual_gemini_api_key_here
```
[![Animation.gif](https://i.postimg.cc/vHqsyCSH/Animation.gif)](https://postimg.cc/zVgMS2r9)


## How to Run the App

With your virtual environment active, launch the application by running:
```bash
streamlit run app.py
```
*(Replace `app.py` with the actual name of your Python file if it is named differently).*

A browser tab should open automatically at `http://localhost:8501`. If it doesn't, copy and paste that URL into your browser.

---

## Project Structure

```text
├── app.py          # The main Streamlit application code
├── .env            # Local configuration file containing API keys (do not commit to Git)
└── README.md       # Project documentation
```

---

## Built With

- [Streamlit](https://streamlit.io) - The fastest way to build and share data apps.
- [LangChain](https://langchain.com) - Framework for developing applications powered by language models.
- [Google Gemini](https://google.dev) - Google's next-generation conversational AI infrastructure.

# AI API Integration Project

## Overview  
This project demonstrates the integration of multiple AI services including Groq, Ollama, Hugging Face, Google Gemini, and Cohere. It provides a simple and unified way to interact with different AI models using Python.

---

## Setup Instructions  

1. Clone or download the project  

2. Install dependencies:  
pip install -r requirements.txt  

3. Create a `.env` file in the project folder and add your API keys:  
GROQ_API_KEY=your_key  
HUGGINGFACE_API_KEY=your_key  
GOOGLE_API_KEY=your_key  
COHERE_API_KEY=your_key  

---

## How to Run  

Run each script individually:  

python groq_example.py  
python ollama_example.py  
python huggingface_example.py  
python gemini_example.py  
python cohere_example.py  

---

## Features  

- Takes user input dynamically  
- Integrates multiple AI APIs in one project  
- Uses environment variables for secure key storage  
- Includes basic error handling  

---

## Multi-API System  

A unified script is included which:  
- Allows users to choose the API  
- Accepts input prompts  
- Returns responses from the selected AI model  

---

## Outputs  

Sample outputs are available in the `screenshots` folder.  

---

## Notes  

- API keys are not hardcoded  
- Ollama runs locally and must be started before use  
- Internet connection is required for cloud APIs  

---

## Additional Info  

This project highlights how multiple AI APIs can be combined into a single system, making it easier to compare and use different models efficiently.
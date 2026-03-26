import os
import requests
from dotenv import load_dotenv
from google import genai  

# Load environment variables
load_dotenv()

# API KEYS
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=GOOGLE_API_KEY)

# Hugging Face URL
HF_API_URL = "https://router.huggingface.co/v1/chat/completions"


# ---------------- GEMINI ----------------
def query_gemini(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash-latest",   
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"Gemini Error: {e}"


# ---------------- HUGGING FACE ----------------
def query_huggingface(prompt):
    try:
        headers = {
            "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "openai/gpt-oss-20b",
            "messages": [
                {"role": "system", "content": "Give direct answers only."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 100
        }

        response = requests.post(HF_API_URL, headers=headers, json=payload)

        if response.status_code != 200:
            return f"HF Error {response.status_code}: {response.text}"

        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"HuggingFace Error: {e}"


# ---------------- MAIN ----------------
if __name__ == "__main__":
    print("=== Multi API Query (Gemini + HuggingFace) ===")

    user_prompt = input("Enter your prompt: ")

    print("\n🔵 Gemini Response:\n")
    print(query_gemini(user_prompt))

    print("\n🟣 Hugging Face Response:\n")
    print(query_huggingface(user_prompt))
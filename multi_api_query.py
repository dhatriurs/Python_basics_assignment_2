import os
import requests
from groq import Groq
import google.generativeai as genai
import cohere
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize clients
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))

HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")


# ---------------- GROQ ----------------
def query_groq(prompt):
    try:
        response = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=300
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Groq Error: {e}"


# ---------------- OLLAMA ----------------
def query_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )
        data = response.json()
        return data.get("response", "No response")
    except Exception as e:
        return f"Ollama Error: {e}"


# ---------------- HUGGING FACE ----------------
API_URL = "https://router.huggingface.co/v1/chat/completions"


def query_huggingface(prompt):
    try:
        headers = {
            "Authorization": f"Bearer {HF_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "openai/gpt-oss-20b",
            "messages": [
                {"role": "system", "content": "Give direct answers only. Do not include reasoning."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 100,
            "temperature": 0.7
        }

        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code != 200:
            return f"HTTP {response.status_code}: {response.text}"

        data = response.json()

        # Case 1: Standard OpenAI format
        if "choices" in data:
            message = data["choices"][0].get("message", {})

            # Try content first
            content = message.get("content", "").strip()

            # If content is empty, use reasoning
            if not content:
                content = message.get("reasoning", "").strip()

            # Final fallback
            if not content:
                return "No usable response generated."

            return content

        # Case 2: Some models return 'text'
        if "choices" in data and "text" in data["choices"][0]:
            return data["choices"][0]["text"]

        # Case 3: Direct text response
        if "text" in data:
            return data["text"]

        # Case 4: fallback → show raw
        return f"No proper content. Raw response:\n{data}"

    except Exception as e:
        return f"Error: {e}"


# ---------------- GEMINI ----------------
def query_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-3.1-flash-lite-preview")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini Error: {e}"


# ---------------- COHERE ----------------
def query_cohere(prompt):
    try:
        response = cohere_client.chat(
            model="command-a-03-2025",
            message=prompt,
            temperature=0.7,
            max_tokens=300
        )

        return response.text.strip()

    except Exception as e:
        return f"Cohere Error: {e}"


# ---------------- MENU SYSTEM ----------------
def show_menu():
    print("\n===== MULTI API QUERY SYSTEM =====")
    print("1. Groq")
    print("2. Ollama (Local)")
    print("3. Hugging Face")
    print("4. Google Gemini")
    print("5. Cohere")
    print("6. Exit")


def main():
    while True:
        show_menu()

        choice = input("Select API (1-6): ")

        if choice == "6":
            print("Exiting program...")
            break

        prompt = input("\nEnter your prompt: ")

        print("\nProcessing...\n")

        if choice == "1":
            result = query_groq(prompt)
        elif choice == "2":
            result = query_ollama(prompt)
        elif choice == "3":
            result = query_huggingface(prompt)
        elif choice == "4":
            result = query_gemini(prompt)
        elif choice == "5":
            result = query_cohere(prompt)
        else:
            print("Invalid choice! Try again.")
            continue

        print("Response:\n")
        print(result)
        print("\n" + "="*50)


# Run program
if __name__ == "__main__":
    main()
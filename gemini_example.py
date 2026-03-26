import os
from google import genai
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Initialize client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def query_gemini(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite-preview",
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("=== Gemini API (WORKING) ===")

    user_prompt = input("Enter your prompt: ")

    print("\nQuerying Gemini...\n")

    result = query_gemini(user_prompt)

    print("Response:\n")
    print(result)
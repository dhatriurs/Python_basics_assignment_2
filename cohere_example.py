import os
import cohere
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Cohere client
co = cohere.Client(os.getenv("COHERE_API_KEY"))


def query_cohere(prompt):
    """
    Query Cohere using latest Chat API
    """

    try:
        response = co.chat(
            model="command-a-03-2025",   
            message=prompt,
            temperature=0.7,
            max_tokens=300
        )

        return response.text.strip()

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    print("=== Cohere API ===")

    user_prompt = input("Enter your prompt: ")

    print("\nQuerying Cohere...\n")

    result = query_cohere(user_prompt)

    print("Response:\n")
    print(result)
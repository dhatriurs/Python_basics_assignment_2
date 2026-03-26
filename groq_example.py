import os
from groq import Groq
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Initialize client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def query_groq(prompt):
    """
    Sends prompt to Groq LLM
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    print("=== Groq API ===")

    user_prompt = input("Enter your prompt: ")

    print("\nQuerying Groq...\n")

    result = query_groq(user_prompt)

    print("Response:\n")
    print(result)
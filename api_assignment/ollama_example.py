import requests


def query_ollama(prompt):
    """
    Sends prompt to local Ollama server
    """

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
        return f"Error: {e}"


if __name__ == "__main__":
    print("=== Ollama API ===")

    user_prompt = input("Enter your prompt: ")

    print("\nQuerying Ollama...\n")

    result = query_ollama(user_prompt)

    print("Response:\n")
    print(result)
import openai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

def summarize_text(text):
    """Generates a concise summary of the given text using OpenAI GPT-4 API."""
    openai.api_key = API_KEY

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Summarize the following text in a concise manner:"},
                  {"role": "user", "content": text}],
        max_tokens=100
    )

    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    user_input = input("Enter text to summarize: ")
    result = summarize_text(user_input)
    print("\nSummary:", result)

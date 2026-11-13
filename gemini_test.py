
import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key not found. Check your .env file.")
else:
    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents="Explain Python in simple words in 3 sentences."
        )

        print("\nGemini API connected successfully!")
        print("\nAI Response:")
        print(response.text)

        client.close()

    except Exception as error:
        print("\nGemini API connection failed.")
        print("Error:", error)

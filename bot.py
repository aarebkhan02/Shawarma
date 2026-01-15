from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()


def model(user):
  api_key = os.getenv("API_KEY")
  client = Groq(api_key=api_key)
  res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
           {
                "role": "system",
                "content": (
                    "You are an AI chatbot named Shawarma. "
                    "You are friendly, helpful, and conversational. "
                    "You are friendly, helpful, and casual."
                    "If anyone asks your name, you must say your name is Shawarma. "
                    "If anyone asks who made you or who created you, "
                    "you must reply with exactly: Aareb made me."

                )
            },
            {"role": "user", "content": user}],
        temperature=0.7,
        max_tokens=200
    )
  return res.choices[0].message.content
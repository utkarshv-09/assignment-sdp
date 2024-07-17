import os
from dotenv import load_dotenv

load_dotenv()
from groq import Groq


class chatBot:
    def __init__(self,message):
        self.client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )
        self.message = message

    def chat_completion(self):
        chat_completion = self.client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": self.message,
            }
        ],
        model="llama3-8b-8192",
    )

        return chat_completion.choices[0].message.content

import os

from dotenv import load_dotenv
from Providers.groq_provider import GroqProvider


load_dotenv()


class ChatModule:

    def __init__(self):

        self.client = GroqProvider()

        self.conversation = [
            {
                "role": "system",
                "content": (
                    "You are a helpful collaborative planning partner. "
                    "Your goal is to understand the user's goals and "
                    "help them develop useful plans."
                )
            }
        ]

    def send_message(self, user_message):

        self.conversation.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation
        )

        assistant_message = response.choices[0].message.content

        self.conversation.append(
            {
                "role": "assistant",
                "content": assistant_message
            }
        )

        return assistant_message
import os

from dotenv import load_dotenv
from groq import Groq

from .llm_provider import LLMProvider


load_dotenv()


class GroqProvider(LLMProvider):

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

        self.model = "openai/gpt-oss-120b"

    def generate_response(self, messages):

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )

        return response.choices[0].message.content
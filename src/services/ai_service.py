from groq import Groq
import streamlit as st


class AIService:

    def __init__(self):

        self.client = Groq(
            api_key=st.secrets["GROQ_API_KEY"]
        )

    def generate_response(self, prompt):

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content
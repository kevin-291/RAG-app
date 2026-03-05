from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_llm(query: str, context: str):
    try:
        system_prompt = f"You are a helpful assistant who analyses documents. Provide the answer strictly based on the attached context"
        user_message = f"Context: \n{context}\n\n Query: \n{query}"

        completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
            model="llama-3.3-70b-versatile"
        )

        return completion.choices[0].message.content
    
    except Exception as e:
        raise Exception(f"Groq API Error occurred: {e}")
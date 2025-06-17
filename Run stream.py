#stream
import os
import asyncio
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env fios.getenv("GOOGLE_API_KEY")le
load_dotenv()
genai.configure(api_key="AIzaSyDhD_WyAAS7eXi44gz1dvaWmqYlL9U_ah0")

async def runstream(prompt):
    print("\n[Run] stream()")
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        stream = await model.generate_content_async(prompt, stream=True)
        
        # Print each chunk without extra newlines
        async for chunk in stream:
            print(chunk.text, end="", flush=True)  # flush=True فوری پرنٹ کرنے کے لیے
        
        print()  # آخر میں ایک نئی لائن کے لیے
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    try:
        prompt = input("📝 Enter your point: ")
        asyncio.run(runstream(prompt))
    except KeyboardInterrupt:
        print("\n❌ User stopped the program!")
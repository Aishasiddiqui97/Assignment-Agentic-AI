import os
import asyncio
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a Gemini Flash agent
agent = genai.GenerativeModel("gemini-1.5-flash")

# User Prompt
prompt = input("📝 Enter your prompt: ")

async def agent_stream():
    print("\n[Agent Level] stream()")
    stream = await agent.generate_content_async(prompt, stream=True)
    async for chunk in stream:
        print(chunk.text, end="")
        print()


if __name__ == "__main__":
  asyncio.run(agent_stream())



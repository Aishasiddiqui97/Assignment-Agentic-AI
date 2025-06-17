import os
import asyncio
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()
genai.configure(api_key="AIzaSyDhD_WyAAS7eXi44gz1dvaWmqYlL9U_ah0")

agent =genai.GenerativeModel("gemini-1.5-flash")
prompt = input("Enter your point: ")

async def agent_run():
    print("\n[Agent Level] run()")
    response = await agent.generate_content_async(prompt)
    print(response.text)

   
if __name__ == "__main__":
    asyncio.run(agent_run())
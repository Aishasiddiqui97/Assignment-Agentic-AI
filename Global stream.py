
# #RUN
# import asyncio
# from dotenv import A
# from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

# gemini_api_key = "AIzaSyDhD_WyAAS7eXi44gz1dvaWmqYlL9U_ah0"

# client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# set_tracing_disabled(disabled=True)

# async def main():
#     print("Running...")  # Debug print
#     agent = Agent(
#         name="POGO",
#         instructions="A help full Assistant.",
#         model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
#     )

#     result = await Runner.run(
#         agent,
#         "Can you write a ayatal qurasi with translate in urdu ")
#     print(result.final_output)

# asyncio.run(main())

# 3️⃣ Global Level
# ---------------------------
import os
import asyncio
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()
genai.configure(api_key="AIzaSyDhD_WyAAS7eXi44gz1dvaWmqYlL9U_ah0")

agent =genai.GenerativeModel("gemini-1.5-flash")
prompt = input("Enter your point: ")

async def global_stream():
    print("\n[Global Level] stream()")
    stream = await genai.GenerativeModel(model_name="gemini-1.5-flash").generate_content_async(prompt, stream=True)
    async for chunk in stream:
        print(chunk.text, end="")
   
if __name__ == "__main__":
    asyncio.run(global_stream())
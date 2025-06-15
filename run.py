#RUN
import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

gemini_api_key = "AIzaSyDhD_WyAAS7eXi44gz1dvaWmqYlL9U_ah0"

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_tracing_disabled(disabled=True)

async def main():
    print("Running...")  # Debug print
    agent = Agent(
        name="POGO",
        instructions="A help full Assistant.",
        model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
    )

    result = await Runner.run(
        agent,
        "Can you write a ayatal qurasi with translate in urdu ")
    print(result.final_output)

asyncio.run(main())


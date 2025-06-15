#RUN.SYNC
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

gemini_api_key = "AIzaSyDhD_WyAAS7eXi44gz1dvaWmqYlL9U_ah0"

#Reference: https://ai.google.dev/gemini-api/docs/openai
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_tracing_disabled(disabled=True)

#async def main():
    # This agent will use the custom LLM provider
agent = Agent(
        name="wasoli bahi",
        instructions="funny answers",
        model=OpenAIChatCompletionsModel(  
            model="gemini-2.0-flash",
            openai_client=client),
)

result = Runner.run_sync(
        agent,
        " romantic movies dialouges in urdu" 
    )
print("run_sync",result.final_output)


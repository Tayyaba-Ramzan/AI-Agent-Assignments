from agents import Agent, ModelSettings
from my_tools.sentiment_tool import sentiment_tool

sentiment_agent = Agent(
    name="sentiment_agent",
    instructions="You analyze the sentiment of user messages.",
    tools=[sentiment_tool],
    model_settings=ModelSettings(
        tool_choice="auto"
    )
)

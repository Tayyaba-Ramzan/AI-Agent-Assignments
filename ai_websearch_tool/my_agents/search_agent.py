from agents import Agent
from my_tools.web_search_tool import tavily_search

def create_search_agent():
    return Agent(
        name="web_search_agent",
        instructions="You are a helpful assistant that answers queries using web search.",
        tools=[tavily_search]
    )

import os
from dotenv import load_dotenv
from agents import Runner
from my_agents.search_agent import create_search_agent

load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

res = Runner.run_sync(starting_agent=create_search_agent(), input="Latest news about Artificial Intelligence")
print("🔍 Final Answer =>", res.final_output)



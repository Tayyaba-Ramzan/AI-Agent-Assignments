import requests
import os
from dotenv import load_dotenv
from agents import function_tool

load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

@function_tool
def tavily_search(query: str) -> str:
    """
    Perform a web search using Tavily API.
    Args:
        query (str): User query
    Returns:
        str: Concatenated search results
    """
    url = "https://api.tavily.com/search"
    headers = {"Authorization": f"Bearer {TAVILY_API_KEY}"}
    payload = {"query": query, "num_results": 3}  # 3 results only

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        results = [item["content"] for item in data.get("results", [])]
        return "\n\n".join(results) if results else "No results found."
    except Exception as e:
        return f"Error fetching search results: {str(e)}"

import asyncio
from agents import Runner
from my_agents.support_agent import support_agent
from my_agents.handoff_agent import handoff_agent
from guardrails.guardrail_agent import guardrail_agent
from my_agents.sentiment_agent import sentiment_agent   # ✅ tool ki jagah agent
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("OPENAI_API_KEY")

async def main():
    print("🤖 Customer Support Bot Ready!")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye! 👋")
            break

        # Guardrail check
        guardrail_output = await Runner.run(guardrail_agent, user_input)
        if "offensive" in guardrail_output.final_output.lower():
            print("Bot: Please rephrase your message politely.")
            continue

        # Sentiment check
        sentiment = await Runner.run(sentiment_agent, user_input)   # ✅ updated
        if sentiment.final_output == "negative":
            result = await Runner.run(handoff_agent, user_input)
            print(f"👩‍💻 Human Agent: {result.final_output}")
            continue

        # Run support agent
        result = await Runner.run(support_agent, user_input)
        print(f"Bot: {result.final_output}")

if __name__ == "__main__":
    asyncio.run(main())

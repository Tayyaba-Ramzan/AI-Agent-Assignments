from agents import Runner,InputGuardrailTripwireTriggered,OutputGuardrailTripwireTriggered
from my_agents.guardrial_agent import general_agent
from dotenv import load_dotenv
import os

load_dotenv()
key=os.getenv("OPENAI_API_KEY")

try:
    msg = input("Enter your question : ")
    result = Runner.run_sync(general_agent, msg)
    print(f"\n\n final output : {result.final_output}")

except InputGuardrailTripwireTriggered:
    print("❌ Error: invalid input (only math allowed).")

except OutputGuardrailTripwireTriggered:
    print("❌ Error: response contained restricted political content.")
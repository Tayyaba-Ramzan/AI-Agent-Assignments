from agents import Agent
from guardrial_function.ouput_guardrial_function import check_output


general_agent = Agent(
    "GeneralAgent",
    instructions="You are a helpful agent",
    output_guardrails=[check_output]
)

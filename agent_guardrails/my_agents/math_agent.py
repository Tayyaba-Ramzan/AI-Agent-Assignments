from agents import Agent
from guardrial_function.input_guardrial_function import check_input

math_agent = Agent(
    "MathAgent",
    input_guardrails=[check_input],
)
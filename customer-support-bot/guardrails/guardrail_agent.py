from agents import Agent

guardrail_agent = Agent(
    name="guardrail_agent",
    instructions=(
        "If user input contains offensive or negative language, politely rephrase "
        "or block it to ensure a positive interaction."
    )
)

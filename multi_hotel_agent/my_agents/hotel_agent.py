from agents import Agent
from guardrial_function.hotel_guardrial_input_function import guardrial_input_function
from instructions.dynamic_instruction import get_hotel_instructions

def create_hotel_agent(hotel_name: str) -> Agent:
    """Create a hotel agent dynamically for a given hotel"""
    return Agent(
        name=f"{hotel_name} Assistant",
        instructions=get_hotel_instructions(hotel_name),
        input_guardrails=[guardrial_input_function],
        output_guardrails=[],
    )

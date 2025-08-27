from agents import Runner,InputGuardrailTripwireTriggered
from my_agents.hotel_agent import create_hotel_agent
from dotenv import load_dotenv
import os
from instructions.dynamic_instruction import get_hotel_instructions
from my_datatypes.hotel_datatypes import hotels_data


load_dotenv()
key=os.getenv("OPENAI_API_KEY")


hotel_name = "Hotel Crown"  
instructions = get_hotel_instructions(hotel_name)
hotel_assistant = create_hotel_agent(instructions)

context = hotels_data[hotel_name]

try:
    res = Runner.run_sync(
        starting_agent=hotel_assistant,
        input="Hotel Crown k owner ka kya name hai?",
        context=context
    )

    print("Final Output =>", res.final_output)

except InputGuardrailTripwireTriggered as e:
    print(f"input trip wire triggered")
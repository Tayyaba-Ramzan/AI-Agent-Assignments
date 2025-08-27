from agents import RunContextWrapper,Agent,GuardrailFunctionOutput,TResponseInputItem,input_guardrail,Runner
from my_datatypes.input_datatypes import MathOutPut
from typing import Any

@input_guardrail
async def check_input(
    ctx: RunContextWrapper[Any], agent: Agent[Any], input_data: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    input_agent = Agent(
        "InputGuardrailAgent",
        instructions="Check and verify if input is related to math",
        output_type=MathOutPut,
    )
    result = await Runner.run(input_agent, input_data, context=ctx.context)
    final_output = result.final_output

    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=not final_output.is_math,
    )
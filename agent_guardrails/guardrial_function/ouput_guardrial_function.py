from agents import RunContextWrapper,GuardrailFunctionOutput,TResponseInputItem,Agent,output_guardrail
from typing import Any
from my_datatypes.output_datatypes import SafeOutput

@output_guardrail
async def check_output(
    ctx: RunContextWrapper[Any], agent: Agent[Any], input_data: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    """
    Guardrail: block responses that mention politics or political figures
    """
    banned_keywords = ["politics", "political", "election", "government",
                       "president", "prime minister", "minister", "trump", "biden",
                       "imran khan", "modi", "putin"]

    # Convert input to string for scanning
    if isinstance(input_data, list):
        text_output = " ".join([str(item) for item in input_data])
    else:
        text_output = str(input_data).lower()

    # Check for banned keywords
    trigger = any(word in text_output.lower() for word in banned_keywords)

    return GuardrailFunctionOutput(
        output_info=SafeOutput( # type: ignore
            is_safe=not trigger,
            reason="Contains political content" if trigger else "Safe output",
        ),
        tripwire_triggered=trigger,
    )

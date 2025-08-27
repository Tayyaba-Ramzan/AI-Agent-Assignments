from agents import input_guardrail,RunContextWrapper,GuardrailFunctionOutput,Runner
from my_agents.guardrial_agent import guardrial_agent

@input_guardrail
async def guardrial_input_function(ctx:RunContextWrapper,agent,input):
  
    result = await Runner.run(guardrial_agent, input=input, context=ctx.context )

    return GuardrailFunctionOutput(
        output_info=not result.final_output,
        tripwire_triggered=False
    )
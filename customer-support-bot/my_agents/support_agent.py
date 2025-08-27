from agents import Agent
from my_tools.faq_tool import faq_tool
from my_tools.order_tool import order_status_tool
from my_tools.sentiment_tool import sentiment_tool
from my_agents.handoff_agent import handoff_agent
from guardrails.guardrail_agent import guardrail_agent
from agents import ModelSettings

support_agent = Agent(
    name="support_agent",
    instructions="You are a helpful support assistant. You can answer FAQs and help with order tracking.",
    tools=[faq_tool, order_status_tool, sentiment_tool],
    model_settings=ModelSettings(
        tool_choice="auto",
        metadata={"team": "support-bot"}
    )
)


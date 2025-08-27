from agents import function_tool, RunContextWrapper

FAQS = {
    "return policy": "You can return products within 30 days of purchase.",
    "shipping": "We offer free shipping on orders above $50.",
    "warranty": "Our products come with a 1-year warranty."
}

@function_tool
def faq_tool(ctx: RunContextWrapper, query: str) -> str:
    """Answer basic product FAQs"""
    for key, value in FAQS.items():
        if key in query.lower():
            return value
    return "Sorry, I don’t know that. Let me connect you to a human agent."

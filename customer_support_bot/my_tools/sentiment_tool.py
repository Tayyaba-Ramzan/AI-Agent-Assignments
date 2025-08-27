from agents import function_tool, RunContextWrapper

@function_tool
def sentiment_tool(ctx: RunContextWrapper, user_message: str) -> str:
    """Simple sentiment check: detect negativity"""
    negatives = ["bad", "worst", "hate", "angry", "upset"]
    if any(word in user_message.lower() for word in negatives):
        return "negative"
    return "positive"

from agents import function_tool, RunContextWrapper
import random

@function_tool
def order_status_tool(ctx: RunContextWrapper, order_id: str) -> str:
    """Fetch simulated order status"""
    statuses = ["Processing", "Shipped", "Out for delivery", "Delivered"]
    return f"Order {order_id} status: {random.choice(statuses)}"

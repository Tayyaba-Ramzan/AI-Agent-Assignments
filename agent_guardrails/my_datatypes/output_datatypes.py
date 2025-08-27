from pydantic import BaseModel

class SafeOutput(BaseModel):
    is_safe: bool
    reason: str
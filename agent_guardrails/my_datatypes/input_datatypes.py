from pydantic import BaseModel

class MathOutPut(BaseModel):
    is_math: bool
    reason: str

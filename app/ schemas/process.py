from pydantic import BaseModel

class RowSchema(BaseModel):
    age: int
    height: float
    weight: float


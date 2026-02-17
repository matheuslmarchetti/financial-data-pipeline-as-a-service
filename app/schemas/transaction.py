from pydantic import BaseModel
from typing import List

class TransactionCreate(BaseModel):
    description: str
    amount: float


class TransactionResponse(BaseModel):
    id: int
    description: str
    amount: float
    user_id: int

    class Config:
        from_attributes = True

class TransactionListResponse(BaseModel):
    total: int
    skip: int
    limit: int
    items: List[TransactionResponse]

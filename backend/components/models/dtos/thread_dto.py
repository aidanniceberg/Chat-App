from pydantic import BaseModel

class ThreadDTO(BaseModel):
    id: int
    user1: int
    user2: int
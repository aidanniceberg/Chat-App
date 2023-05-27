from datetime import datetime

from pydantic import BaseModel


class MessageDTO(BaseModel):
    id: int
    group: bool
    thread_id: int
    sender: int
    content: str
    timestamp: datetime
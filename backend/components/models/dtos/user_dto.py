from datetime import date
from typing import Optional

from pydantic import BaseModel


class UserDTO(BaseModel):
    id: int
    username: str
    first_name: str = ""
    last_name: str = ""
    password: str
    birthday: Optional[date] = None
    email: Optional[str] = None

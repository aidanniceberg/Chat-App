from pydantic import BaseModel, validator

from typing import List

class GroupThreadDTO(BaseModel):
    id: int
    users: List[int]

    @validator("users", pre=True)
    def parse_users(cls, u):
        try:
            return [int(id) for id in u.split(" ")] if type(u) is str else u
        except Exception as e:
            raise TypeError(f"Invalid type for users. {e}")

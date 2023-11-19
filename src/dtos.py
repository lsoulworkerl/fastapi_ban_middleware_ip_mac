from pydantic import BaseModel


class VoteDTO(BaseModel):
    vote: bool

    class Config:
        from_attributes = True

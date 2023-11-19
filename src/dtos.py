from pydantic import BaseModel


class TestDTO(BaseModel):
    test: str

    class Config:
        from_attributes = True

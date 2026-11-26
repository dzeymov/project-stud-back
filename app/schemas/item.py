from pydantic import BaseModel


class ItemCreate(BaseModel):
    title: str
    description: str = ""


class ItemRead(BaseModel):
    id: int
    title: str
    description: str
    owner_id: int

    model_config = {"from_attributes": True}
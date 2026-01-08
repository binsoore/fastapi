from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class ItemBase(BaseModel):
    """
    Base item schema
    """
    title: str
    description: Optional[str] = None
    price: float


class ItemCreate(ItemBase):
    """
    Schema for creating an item
    """
    pass


class ItemUpdate(BaseModel):
    """
    Schema for updating an item
    """
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    is_available: Optional[bool] = None


class ItemResponse(ItemBase):
    """
    Schema for item response
    """
    id: int
    is_available: bool
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

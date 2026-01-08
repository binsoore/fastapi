from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.config.database import get_db
from app.schemas.item import ItemCreate, ItemUpdate, ItemResponse
from app.schemas.common import MessageResponse
from app.impl.item_impl import ItemImpl

router = APIRouter(
    prefix="/items",
    tags=["items"]
)


@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(
    item: ItemCreate,
    owner_id: int,
    db: Session = Depends(get_db)
):
    """
    Create a new item
    """
    return ItemImpl.create_item(db=db, item=item, owner_id=owner_id)


@router.get("/", response_model=List[ItemResponse])
def get_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Get list of items
    """
    items = ItemImpl.get_items(db, skip=skip, limit=limit)
    return items


@router.get("/owner/{owner_id}", response_model=List[ItemResponse])
def get_items_by_owner(
    owner_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Get items by owner
    """
    items = ItemImpl.get_items_by_owner(db, owner_id=owner_id, skip=skip, limit=limit)
    return items


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    """
    Get item by ID
    """
    db_item = ItemImpl.get_item_by_id(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    return db_item


@router.put("/{item_id}", response_model=ItemResponse)
def update_item(
    item_id: int,
    item: ItemUpdate,
    db: Session = Depends(get_db)
):
    """
    Update item
    """
    db_item = ItemImpl.update_item(db, item_id=item_id, item_update=item)
    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    return db_item


@router.delete("/{item_id}", response_model=MessageResponse)
def delete_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete item
    """
    success = ItemImpl.delete_item(db, item_id=item_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    return MessageResponse(message="Item deleted successfully")

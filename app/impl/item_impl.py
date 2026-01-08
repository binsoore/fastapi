from sqlalchemy.orm import Session
from typing import Optional, List
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate


class ItemImpl:
    """
    Item implementation/service layer
    """

    @staticmethod
    def get_item_by_id(db: Session, item_id: int) -> Optional[Item]:
        """Get item by ID"""
        return db.query(Item).filter(Item.id == item_id).first()

    @staticmethod
    def get_items(db: Session, skip: int = 0, limit: int = 100) -> List[Item]:
        """Get list of items"""
        return db.query(Item).offset(skip).limit(limit).all()

    @staticmethod
    def get_items_by_owner(db: Session, owner_id: int, skip: int = 0, limit: int = 100) -> List[Item]:
        """Get items by owner"""
        return db.query(Item).filter(Item.owner_id == owner_id).offset(skip).limit(limit).all()

    @staticmethod
    def create_item(db: Session, item: ItemCreate, owner_id: int) -> Item:
        """Create a new item"""
        db_item = Item(
            **item.model_dump(),
            owner_id=owner_id
        )
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    @staticmethod
    def update_item(db: Session, item_id: int, item_update: ItemUpdate) -> Optional[Item]:
        """Update an item"""
        db_item = ItemImpl.get_item_by_id(db, item_id)
        if not db_item:
            return None

        update_data = item_update.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(db_item, field, value)

        db.commit()
        db.refresh(db_item)
        return db_item

    @staticmethod
    def delete_item(db: Session, item_id: int) -> bool:
        """Delete an item"""
        db_item = ItemImpl.get_item_by_id(db, item_id)
        if not db_item:
            return False

        db.delete(db_item)
        db.commit()
        return True

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Item
from starlette import status

router = APIRouter(
    prefix='/items',
    tags=['items']
)


class ItemModel(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class CreateItemModel(BaseModel):
    title: str

    class Config:
        orm_mode = True


@router.get('/', response_model=list[ItemModel], status_code=status.HTTP_200_OK)
def list_items(db: Session = Depends(get_db)):
    return db.query(Item).all()


@router.post('/', response_model=ItemModel, status_code=status.HTTP_201_CREATED)
def create_item(item_model: CreateItemModel, db: Session = Depends(get_db)):
    new_item = Item(**item_model.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item


@router.get('/{id}', response_model=ItemModel, status_code=status.HTTP_200_OK)
def get_item(id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == id).first()
    if item is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Item not found for id: {id}")
    return item


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_item(id: int, db: Session = Depends(get_db)):
    deleted_item = db.query(Item).filter(Item.id == id)
    if deleted_item.first() is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Item not found for id: {id}")
    deleted_item.delete(synchronize_session=False)
    db.commit()

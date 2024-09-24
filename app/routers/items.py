from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Item


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/items/')
def create_item(item: Item, db: Session = Depends(get_db)):
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.delete('/items/{item_id}')
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    db.delete(item)
    db.commit()
    return {'message': 'Item delated'}

@router.get('/items/')
def get_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = db.query(Item).offset(skip).limit(limit).all()
    return items


@router.get("/items/{item_id}/history/")
def get_item_history(item_id: int, db: Session = Depends(get_db)):
    # Проверим, существует ли товар с данным item_id
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    # Получаем историю цен для данного товара
    price_history = db.query(PriceHistory).filter(PriceHistory.item_id == item_id).order_by(
        PriceHistory.timestamp.desc()).all()

    # Если история пустая
    if not price_history:
        raise HTTPException(status_code=404, detail="Price history not found")

    # Формируем список истории цен
    history = [
        {"price": record.price, "timestamp": record.timestamp}
        for record in price_history
    ]

    return {
        "item_id": item_id,
        "item_name": item.name,
        "price_history": history
    }

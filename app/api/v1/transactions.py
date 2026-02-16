from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.transaction_service import create_transaction

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create(
    description: str,
    amount: float,
    db: Session = Depends(get_db)
):
    transaction = create_transaction(
        db=db,
        description=description,
        amount=amount
    )

    return {
        "id": transaction.id,
        "description": transaction.description,
        "amount": transaction.amount
    }

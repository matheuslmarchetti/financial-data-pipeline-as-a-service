from sqlalchemy.orm import Session
from typing import List
from app.models.transaction import Transaction
from sqlalchemy.exc import SQLAlchemyError



def create_transaction(
    db: Session,
    description: str,
    amount: float,
    user_id: int
) -> Transaction:
    if amount <= 0:
        raise ValueError("Amount must be greater than zero")
    try:
        transaction = Transaction(
            description=description,
            amount=amount,
            user_id=user_id
        )

        db.add(transaction)
        db.commit()
        db.refresh(transaction)

        return transaction

    except SQLAlchemyError:
        db.rollback()
        raise


def get_transactions(
    db: Session,
    skip: int = 0,
    limit: int = 10
):
    query = db.query(Transaction)

    total = query.count()

    items = (
        query
        .offset(skip)
        .limit(limit)
        .all()
    )

    return {
        "total": total,
        "items": items,
        "skip": skip,
        "limit": limit
    }
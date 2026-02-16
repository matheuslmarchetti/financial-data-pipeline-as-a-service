from sqlalchemy.orm import Session
from app.models.transaction import Transaction


def create_transaction(
    db: Session,
    description: str,
    amount: float
) -> Transaction:

    transaction = Transaction(
        description=description,
        amount=amount
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.transaction import (
    TransactionCreate,
    TransactionResponse,
)
from app.services.transaction_service import (
    create_transaction,
    get_transactions
)

from app.schemas.transaction import (
    TransactionCreate,
    TransactionResponse,
    TransactionListResponse
)

from fastapi import HTTPException

router = APIRouter()


@router.post("/", response_model=TransactionResponse)
def create(
    transaction: TransactionCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_transaction(
            db=db,
            description=transaction.description,
            amount=transaction.amount,
            user_id=transaction.user_id
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=TransactionListResponse)
def list_transactions(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return get_transactions(db, skip=skip, limit=limit)
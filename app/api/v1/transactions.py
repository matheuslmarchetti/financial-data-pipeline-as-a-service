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

from app.core.security import get_current_user
from app.models.user import User


router = APIRouter()


@router.post("/", response_model=TransactionResponse)
def create(
    transaction: TransactionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return create_transaction(
            db=db,
            description=transaction.description,
            amount=transaction.amount,
            user_id=current_user.id
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=TransactionListResponse)
def list_transactions(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_transactions(db, skip=skip, limit=limit)
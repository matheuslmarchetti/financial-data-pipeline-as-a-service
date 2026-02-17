from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(
        db=db,
        name=user.name,
        email=user.email,
        password=user.password
    )
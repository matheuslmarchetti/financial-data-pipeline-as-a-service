from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.user import User


def create_user(
    db: Session,
    name: str,
    email: str
) -> User:
    try:
        user = User(name=name, email=email)

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    except SQLAlchemyError:
        db.rollback()
        raise
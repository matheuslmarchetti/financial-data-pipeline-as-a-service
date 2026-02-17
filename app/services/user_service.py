from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.user import User
from app.core.security import get_password_hash



def create_user(
    db: Session,
    name: str,
    email: str,
    password: str
) -> User:
    try:
        user = User(name=name, email=email, password_hash=get_password_hash(password))

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    except SQLAlchemyError:
        db.rollback()
        raise
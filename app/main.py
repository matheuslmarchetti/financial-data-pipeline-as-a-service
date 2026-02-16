from fastapi import FastAPI
from app.api.v1.router import api_router
from app.db.session import engine
from app.db.base import Base
from app.models import transaction  # importante importar model

app = FastAPI(
    title="Financial Data Pipeline API",
    version="1.0.0",
)

app.include_router(api_router, prefix="/api/v1")

Base.metadata.create_all(bind=engine)
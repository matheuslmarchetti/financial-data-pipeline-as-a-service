from fastapi import APIRouter
from app.api.v1.health import router as health_router
from app.api.v1.transactions import router as transactions_router
from app.api.v1.users import router as users_router


api_router = APIRouter()

api_router.include_router(health_router, prefix="/health", tags=["Health"])

api_router.include_router(
    transactions_router,
    prefix="/transactions",
    tags=["Transactions"]
)

api_router.include_router(
    users_router,
    prefix="/users",
    tags=["Users"]
)

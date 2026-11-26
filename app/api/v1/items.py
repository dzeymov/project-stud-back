from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user
from app.database import get_db
from app.models.user import User
from app.schemas.item import ItemCreate, ItemRead
from app.services import item_service

router = APIRouter(prefix="/items", tags=["items"])


@router.post("", response_model=ItemRead, status_code=201)
async def create_item(
    payload: ItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await item_service.create_item(db, current_user.id, payload.title, payload.description)


@router.get("", response_model=list[ItemRead])
async def list_items(
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_user),
):
    return await item_service.list_items(db)
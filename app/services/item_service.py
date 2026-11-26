from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.item import Item
from app.worker import send_notification


async def create_item(db: AsyncSession, owner_id: int, title: str, description: str) -> Item:
    item = Item(title=title, description=description, owner_id=owner_id)
    db.add(item)
    await db.commit()
    await db.refresh(item)
    # Фоновая задача Celery — привязана к реальному действию
    send_notification.delay(item.id, item.title)
    return item


async def list_items(db: AsyncSession) -> list[Item]:
    result = await db.scalars(select(Item))
    return list(result)
from fastapi import APIRouter, Depends

from app.api.deps import get_current_admin
from app.models.user import User

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/ping")
async def admin_ping(_: User = Depends(get_current_admin)):
    return {"status": "admin ok"}
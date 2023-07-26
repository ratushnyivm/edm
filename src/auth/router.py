from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_async_session

router = APIRouter(
    prefix='/users',
    tags=['Auth']
)


@router.get('')
async def get_users(
    user_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    return {'user': user_id}

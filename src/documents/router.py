from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_async_session
from src.documents import repository, schemas

router = APIRouter(
    prefix='/documents',
    tags=['Documents']
)


@router.post('/codes')
async def create_document_code(
    document_code: schemas.DocumentCodeCreate,
    session: AsyncSession = Depends(get_async_session)
):
    code = await repository.create_new_document_code(
        document_code=document_code,
        session=session
    )
    return code


@router.post('/')
async def create_document(
    document: schemas.DocumentCreate,
    session: AsyncSession = Depends(get_async_session)
):
    new_document = await repository.create_new_document(
        document=document,
        session=session
    )
    return new_document

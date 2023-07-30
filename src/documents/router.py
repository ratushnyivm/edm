from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_async_session
from src.documents import repository, schemas

router = APIRouter(
    prefix='/documents',
    tags=['Documents']
)

# Document codes


@router.post('/codes', response_model=schemas.DocumentCodeShow)
async def create_document_code(
    document_code: schemas.DocumentCodeCreate,
    session: AsyncSession = Depends(get_async_session)
):
    new_document_code = await repository.create_new_document_code(
        document_code=document_code,
        session=session
    )
    return new_document_code


@router.get('/codes/{id}', response_model=schemas.DocumentCodeShow)
async def get_document_code(
    id: int,
    session: AsyncSession = Depends(get_async_session)
):
    document_code = await repository.retreive_document_code(
        id=id,
        session=session
    )
    if not document_code:
        raise HTTPException(
            detail=f'Document code with ID {id} does not exist.',
            status_code=status.HTTP_404_NOT_FOUND
        )
    return document_code


@router.get('/codes', response_model=list[schemas.DocumentCodeShow])
async def get_all_document_codes(
    session: AsyncSession = Depends(get_async_session)
):
    document_codes = await repository.list_document_codes(session=session)
    return document_codes


@router.put('/codes/{id}', response_model=schemas.DocumentCodeShow)
async def update_document_code(
    id: int,
    document_code: schemas.DocumentCodeUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    updated_document_code = await repository.update_document_code_in_db(
        id=id,
        document_code=document_code,
        session=session
    )
    if not updated_document_code:
        raise HTTPException(
            detail=f'Document code with ID {id} does not exist.',
            status_code=status.HTTP_404_NOT_FOUND
        )
    return updated_document_code


# Documents


@router.post('', response_model=schemas.DocumentShow)
async def create_document(
    document: schemas.DocumentCreate,
    session: AsyncSession = Depends(get_async_session)
):
    new_document = await repository.create_new_document(
        document=document,
        session=session
    )
    return new_document


@router.get('/{id}', response_model=schemas.DocumentShow)
async def get_document(
    id: int,
    session: AsyncSession = Depends(get_async_session)
):
    document = await repository.retreive_document(
        id=id,
        session=session
    )
    if not document:
        raise HTTPException(
            detail=f'Document with ID {id} does not exist.',
            status_code=status.HTTP_404_NOT_FOUND
        )
    return document


@router.get('', response_model=list[schemas.DocumentShow])
async def get_all_documents(
    session: AsyncSession = Depends(get_async_session)
):
    documents = await repository.list_documents(session=session)
    return documents


@router.put('/{id}', response_model=schemas.DocumentShow)
async def update_document(
    id: int,
    document: schemas.DocumentUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    updated_document = await repository.update_document_in_db(
        id=id,
        document=document,
        session=session
    )
    if not updated_document:
        raise HTTPException(
            detail=f'Document with ID {id} does not exist.',
            status_code=status.HTTP_404_NOT_FOUND
        )
    return updated_document

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.documents import models, schemas

# Document codes


async def get_document_code_list_in_db(
    session: AsyncSession
) -> list[models.DocumentCode]:
    stmt = select(models.DocumentCode)
    document_codes = await session.scalars(stmt)
    return document_codes


async def create_document_code_in_db(
    document_code: schemas.DocumentCodeCreate,
    session: AsyncSession
) -> models.DocumentCode:
    new_document_code = models.DocumentCode(
        code=document_code.code
    )
    session.add(new_document_code)
    await session.commit()
    await session.refresh(new_document_code)

    return new_document_code


async def get_document_code_in_db(
    id: int,
    session: AsyncSession
) -> models.DocumentCode:
    stmt = select(models.DocumentCode).where(models.DocumentCode.id == id)
    document_code = await session.scalar(stmt)
    return document_code


async def update_document_code_in_db(
    id: int,
    document_code: schemas.DocumentCodeUpdate,
    session: AsyncSession
) -> models.DocumentCode:
    stmt = select(models.DocumentCode).where(models.DocumentCode.id == id)
    document_code_in_db = await session.scalar(stmt)

    if not document_code_in_db:
        return

    document_code_in_db.code = document_code.code

    session.add(document_code_in_db)
    await session.commit()
    await session.refresh(document_code_in_db)

    return document_code_in_db


async def delete_document_code_in_db(
    id: int,
    session: AsyncSession
) -> dict[str, str]:
    stmt = select(models.DocumentCode).where(models.DocumentCode.id == id)
    document_code = await session.scalar(stmt)

    if not document_code:
        return {'error': f'Could not find document code with id {id}'}

    await session.delete(document_code)
    await session.commit()

    return {'msg': f'deleted document code with id {id}'}


# Documents

async def get_document_list_in_db(
    session: AsyncSession
) -> list[models.Document]:
    stmt = select(models.Document)
    documents = await session.scalars(stmt)
    return documents


async def create_document_in_db(
    document: schemas.DocumentCreate,
    session: AsyncSession
) -> models.Document:
    new_document = models.Document(
        number=document.number,
        title=document.title,
        document_code_id=document.document_code_id
    )
    session.add(new_document)
    await session.commit()
    await session.refresh(new_document)

    return new_document


async def get_document_in_db(
    id: int,
    session: AsyncSession
) -> models.Document:
    stmt = select(models.Document).where(models.Document.id == id)
    document = await session.scalar(stmt)
    return document


async def update_document_in_db(
    id: int,
    document: schemas.DocumentUpdate,
    session: AsyncSession
) -> models.Document:
    stmt = select(models.Document).where(models.Document.id == id)
    document_in_db = await session.scalar(stmt)

    if not document_in_db:
        return

    document_in_db.number = document.number
    document_in_db.title = document.title
    document_in_db.document_code_id = document.document_code_id

    session.add(document_in_db)
    await session.commit()
    await session.refresh(document_in_db)

    return document_in_db


async def delete_document_in_db(
    id: int,
    session: AsyncSession
) -> dict[str, str]:
    stmt = select(models.Document).where(models.Document.id == id)
    document = await session.scalar(stmt)

    if not document:
        return {'error': f'Could not find document with id {id}'}

    await session.delete(document)
    await session.commit()

    return {'msg': f'deleted document with id {id}'}

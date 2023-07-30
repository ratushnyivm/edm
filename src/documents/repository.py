from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.documents import models, schemas

# Document codes


async def create_new_document_code(
    document_code: schemas.DocumentCodeCreate,
    session: AsyncSession
) -> models.DocumentCode:
    new_document_code = models.DocumentCode(
        id=document_code.id,
        code=document_code.code
    )
    session.add(new_document_code)
    await session.commit()
    await session.refresh(new_document_code)

    return new_document_code


async def retreive_document_code(
    id: int,
    session: AsyncSession
) -> models.DocumentCode:
    stmt = select(models.DocumentCode).where(models.DocumentCode.id == id)
    document_code = await session.scalar(stmt)
    return document_code


async def list_document_codes(
    session: AsyncSession
) -> list[models.DocumentCode]:
    stmt = select(models.DocumentCode)
    document_codes = await session.scalars(stmt)
    return document_codes


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

    return document_code_in_db


# Documents


async def create_new_document(
    document: schemas.DocumentCreate,
    session: AsyncSession
) -> models.Document:
    new_document = models.Document(
        id=document.id,
        number=document.number,
        title=document.title,
        document_code_id=document.document_code_id
    )
    session.add(new_document)
    await session.commit()
    await session.refresh(new_document)

    return new_document


async def retreive_document(id: int, session: AsyncSession) -> models.Document:
    stmt = select(models.Document).where(models.Document.id == id)
    document = await session.scalar(stmt)
    return document


async def list_documents(session: AsyncSession) -> list[models.Document]:
    stmt = select(models.Document)
    documents = await session.scalars(stmt)
    return documents


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

    return document_in_db

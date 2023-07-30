from sqlalchemy.ext.asyncio import AsyncSession

from src.documents.models import Document, DocumentCode
from src.documents.schemas import DocumentCodeCreate, DocumentCreate


async def create_new_document_code(
    document_code: DocumentCodeCreate,
    session: AsyncSession
) -> DocumentCode:
    new_document_code = DocumentCode(
        id=document_code.id,
        code=document_code.code
    )
    session.add(new_document_code)
    await session.commit()
    await session.refresh(new_document_code)

    return new_document_code


async def create_new_document(
    document: DocumentCreate,
    session: AsyncSession
) -> Document:
    new_document = Document(
        id=document.id,
        number=document.number,
        title=document.title,
        document_code_id=document.document_code_id
    )
    session.add(new_document)
    await session.commit()
    await session.refresh(new_document)

    return new_document

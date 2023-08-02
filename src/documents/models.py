from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base_class import Base


class DocumentCode(Base):
    __tablename__ = 'document_codes'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(
        String(length=5),
        unique=True,
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        onupdate=datetime.now,
        nullable=True
    )

    documents: Mapped[list['Document']] = relationship(
        back_populates='document_code'
    )


class Document(Base):
    __tablename__ = 'documents'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    number: Mapped[str] = mapped_column(String(length=30), nullable=False)
    title: Mapped[str] = mapped_column(String(length=100), nullable=False)
    document_code_id: Mapped[int] = mapped_column(
        ForeignKey('document_codes.id')
    )
    document_code_number: Mapped[Optional[int]] = mapped_column(
        nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        onupdate=datetime.now,
        nullable=True
    )

    document_code: Mapped['DocumentCode'] = relationship(
        back_populates='documents'
    )

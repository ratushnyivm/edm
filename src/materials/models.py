from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base_class import Base


class MaterialCategory(Base):
    __tablename__ = 'material_categories'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(
        String(length=50),
        unique=True,
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        onupdate=datetime.now,
        nullable=True
    )

    materials: Mapped[list['Material']] = relationship(
        back_populates='material_category'
    )


class Material(Base):
    __tablename__ = 'materials'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(length=255), nullable=False)
    material_category_id: Mapped[int] = mapped_column(
        ForeignKey('material_categories.id')
    )
    density: Mapped[int] = mapped_column(default=0)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        onupdate=datetime.now,
        nullable=True
    )

    material_category: Mapped['MaterialCategory'] = relationship(
        back_populates='materials'
    )

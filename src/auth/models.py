from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.base_class import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String)

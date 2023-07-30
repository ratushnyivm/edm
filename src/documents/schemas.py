from datetime import datetime

from pydantic import BaseModel, Field


class DocumentCodeCreate(BaseModel):
    id: int
    code: str = Field(min_length=1, max_length=5)
    created_at: datetime
    updated_at: datetime


class DocumentCreate(BaseModel):
    id: int
    number: str = Field(min_length=1, max_length=30)
    title: str = Field(min_length=1, max_length=100)
    document_code_id: int
    created_at: datetime
    updated_at: datetime

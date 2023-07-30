from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

# Document codes


class DocumentCodeCreate(BaseModel):
    id: int
    code: str = Field(min_length=1, max_length=5)
    created_at: datetime
    updated_at: datetime


class DocumentCodeUpdate(BaseModel):
    code: str = Field(min_length=1, max_length=5)


class DocumentCodeShow(BaseModel):
    id: int
    code: str
    created_at: datetime
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


# Documents


class DocumentCreate(BaseModel):
    id: int
    number: str = Field(min_length=1, max_length=30)
    title: str = Field(min_length=1, max_length=100)
    document_code_id: int
    created_at: datetime
    updated_at: datetime


class DocumentUpdate(BaseModel):
    number: str = Field(min_length=1, max_length=30)
    title: str = Field(min_length=1, max_length=100)
    document_code_id: int


class DocumentShow(BaseModel):
    id: int
    number: str
    title: str
    document_code_id: int
    created_at: datetime
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

# Document codes


class DocumentCodeCreate(BaseModel):
    code: str = Field(min_length=1, max_length=5)


class DocumentCodeUpdate(BaseModel):
    code: str = Field(min_length=1, max_length=5)


class DocumentCodeShow(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    code: str
    created_at: datetime
    updated_at: datetime | None


# Documents


class DocumentCreate(BaseModel):
    number: str = Field(min_length=1, max_length=30)
    title: str = Field(min_length=1, max_length=100)
    document_code_id: int
    document_code_number: int | None = Field('null', ge=1)


class DocumentUpdate(BaseModel):
    number: str = Field(min_length=1, max_length=30)
    title: str = Field(min_length=1, max_length=100)
    document_code_id: int
    document_code_number: int | None = Field('null', ge=1)


class DocumentShow(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    number: str
    title: str
    document_code_id: int
    document_code_number: int | None
    created_at: datetime
    updated_at: datetime | None

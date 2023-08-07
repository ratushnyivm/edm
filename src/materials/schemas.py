from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

# Material categories


class MaterialCategoryCreate(BaseModel):
    title: str = Field(min_length=2, max_length=50)


class MaterialCategoryUpdate(BaseModel):
    title: str = Field(min_length=2, max_length=50)


class MaterialCategoryShow(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    created_at: datetime
    updated_at: datetime | None


# Materials


class MaterialCreate(BaseModel):
    title: str = Field(min_length=2, max_length=255)
    material_category_id: int
    density: int = Field(ge=0)


class MaterialUpdate(BaseModel):
    title: str = Field(min_length=2, max_length=255)
    material_category_id: int
    density: int = Field(ge=0)


class MaterialShow(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    material_category_id: int
    density: int
    created_at: datetime
    updated_at: datetime | None

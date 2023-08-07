from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.materials import models, schemas

# Material categories


async def get_material_category_list_in_db(
    session: AsyncSession
) -> list[models.MaterialCategory]:
    stmt = select(models.MaterialCategory)
    material_categories = await session.scalars(stmt)
    return material_categories


async def create_material_category_in_db(
    material_category: schemas.MaterialCategoryCreate,
    session: AsyncSession
) -> models.MaterialCategory:
    new_material_category = models.MaterialCategory(
        title=material_category.title
    )
    session.add(new_material_category)
    await session.commit()
    await session.refresh(new_material_category)

    return new_material_category


async def get_material_category_in_db(
    id: int,
    session: AsyncSession
) -> models.MaterialCategory:
    stmt = select(models.MaterialCategory)\
        .where(models.MaterialCategory.id == id)
    material_category = await session.scalar(stmt)
    return material_category


async def update_material_category_in_db(
    id: int,
    material_category: schemas.MaterialCategoryUpdate,
    session: AsyncSession
) -> models.MaterialCategory:
    stmt = select(models.MaterialCategory)\
        .where(models.MaterialCategory.id == id)
    material_category_in_db = await session.scalar(stmt)

    if not material_category_in_db:
        return

    material_category_in_db.title = material_category.title

    session.add(material_category_in_db)
    await session.commit()
    await session.refresh(material_category_in_db)

    return material_category_in_db


async def delete_material_category_in_db(
    id: int,
    session: AsyncSession
) -> dict[str, str]:
    stmt = select(models.MaterialCategory)\
        .where(models.MaterialCategory.id == id)
    material_category = await session.scalar(stmt)

    if not material_category:
        return {'error': f'Could not find material caregory with id {id}'}

    await session.delete(material_category)
    await session.commit()

    return {'msg': f'deleted material caregory with id {id}'}


# Materials


async def get_material_list_in_db(
    session: AsyncSession
) -> list[models.Material]:
    stmt = select(models.Material)
    materials = await session.scalars(stmt)
    return materials


async def create_material_in_db(
    material: schemas.MaterialCreate,
    session: AsyncSession
) -> models.Material:
    new_material = models.Material(
        title=material.title,
        material_category_id=material.material_category_id,
        density=material.density
    )
    session.add(new_material)
    await session.commit()
    await session.refresh(new_material)

    return new_material


async def get_material_in_db(
    id: int,
    session: AsyncSession
) -> models.Material:
    stmt = select(models.Material).where(models.Material.id == id)
    material = await session.scalar(stmt)
    return material


async def update_material_in_db(
    id: int,
    material: schemas.MaterialUpdate,
    session: AsyncSession
) -> models.Material:
    stmt = select(models.Material).where(models.Material.id == id)
    material_in_db = await session.scalar(stmt)

    if not material_in_db:
        return

    material_in_db.title = material.title
    material_in_db.material_category_id = material.material_category_id
    material_in_db.density = material.density

    session.add(material_in_db)
    await session.commit()
    await session.refresh(material_in_db)

    return material_in_db


async def delete_material_in_db(
    id: int,
    session: AsyncSession
) -> dict[str, str]:
    stmt = select(models.Material).where(models.Material.id == id)
    material = await session.scalar(stmt)

    if not material:
        return {'error': f'Could not find material with id {id}'}

    await session.delete(material)
    await session.commit()

    return {'msg': f'deleted material with id {id}'}

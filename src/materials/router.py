from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_async_session
from src.materials import repository, schemas

router = APIRouter(
    prefix='/api/materials',
    tags=['Materials']
)

# Material categories


@router.get('/categories', response_model=list[schemas.MaterialCategoryShow])
async def get_material_category_list(
    session: AsyncSession = Depends(get_async_session)
):
    material_categories = await repository.get_material_category_list_in_db(
        session=session
    )
    return material_categories


@router.post('/categories', response_model=schemas.MaterialCategoryShow)
async def create_material_category(
    material_category: schemas.MaterialCategoryCreate,
    session: AsyncSession = Depends(get_async_session)
):
    new_material_category = await repository.create_material_category_in_db(
        material_category=material_category,
        session=session
    )
    return new_material_category


@router.get('/categories/{id}', response_model=schemas.MaterialCategoryShow)
async def get_material_category(
    id: int,
    session: AsyncSession = Depends(get_async_session)
):
    material_category = await repository.get_material_category_in_db(
        id=id,
        session=session
    )
    if not material_category:
        raise HTTPException(
            detail=f'Material category with ID {id} does not exist.',
            status_code=status.HTTP_404_NOT_FOUND
        )
    return material_category


@router.put('/categories/{id}', response_model=schemas.MaterialCategoryShow)
async def update_material_category(
    id: int,
    material_category: schemas.MaterialCategoryUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    updated_material_category = await repository.\
        update_material_category_in_db(
            id=id,
            material_category=material_category,
            session=session
        )
    if not updated_material_category:
        raise HTTPException(
            detail=f'Material category with ID {id} does not exist.',
            status_code=status.HTTP_404_NOT_FOUND
        )
    return updated_material_category


@router.delete('/categories/{id}')
async def delete_material_category(
    id: int,
    session: AsyncSession = Depends(get_async_session)
):
    message = await repository.delete_material_category_in_db(
        id=id,
        session=session
    )
    if message.get('error'):
        raise HTTPException(
            detail=message.get('error'),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    return {'msg': f'Successfully deleted material category with id {id}'}


# Materials


@router.get('', response_model=list[schemas.MaterialShow])
async def get_material_list(
    session: AsyncSession = Depends(get_async_session)
):
    materials = await repository.get_material_list_in_db(session=session)
    return materials


@router.post('', response_model=schemas.MaterialShow)
async def create_material(
    material: schemas.MaterialCreate,
    session: AsyncSession = Depends(get_async_session)
):
    new_material = await repository.create_material_in_db(
        material=material,
        session=session
    )
    return new_material


@router.get('/{id}', response_model=schemas.MaterialShow)
async def get_material(
    id: int,
    session: AsyncSession = Depends(get_async_session)
):
    material = await repository.get_material_in_db(
        id=id,
        session=session
    )
    if not material:
        raise HTTPException(
            detail=f'Material with ID {id} does not exist.',
            status_code=status.HTTP_404_NOT_FOUND
        )
    return material


@router.put('/{id}', response_model=schemas.MaterialShow)
async def update_material(
    id: int,
    material: schemas.MaterialUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    updated_material = await repository.update_material_in_db(
        id=id,
        material=material,
        session=session
    )
    if not updated_material:
        raise HTTPException(
            detail=f'Material with ID {id} does not exist.',
            status_code=status.HTTP_404_NOT_FOUND
        )
    return updated_material


@router.delete('/{id}')
async def delete_material(
    id: int,
    session: AsyncSession = Depends(get_async_session)
):
    message = await repository.delete_material_in_db(
        id=id,
        session=session
    )
    if message.get('error'):
        raise HTTPException(
            detail=message.get('error'),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    return {'msg': f'Successfully deleted material with id {id}'}

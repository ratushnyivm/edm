from typing import Union

from fastapi import FastAPI

from src.core.config import settings
from src.documents.router import router as router_documents

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app.include_router(router_documents)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

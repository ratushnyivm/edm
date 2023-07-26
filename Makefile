install:
	poetry install

start:
	poetry run uvicorn src.main:app --reload

lint:
	poetry run flake8 .

revision:
	alembic revision --autogenerate

upgrade:
	alembic upgrade head

# alembic init -t async migrations

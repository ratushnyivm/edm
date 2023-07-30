install:
	poetry install

start:
	poetry run uvicorn src.main:app --reload

lint:
	poetry run flake8 .

shell:
	poetry run python -i src/main.py

revision:
	poetry run alembic revision --autogenerate

upgrade:
	poetry run alembic upgrade head

# alembic init -t async migrations

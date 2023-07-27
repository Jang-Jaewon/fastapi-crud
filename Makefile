build:
	docker compose build

stop:
	docker compose down

start:
	docker compose up -d

beauty:
	black . && isort .

db-migrate:
	docker-compose exec app alembic revision --autogenerate -m "${MSG}"

db-upgrade:
	docker-compose exec app alembic upgrade head
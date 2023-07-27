build:
	docker compose build

stop:
	docker compose down

start:
	docker compose up -d

beauty:
	black . && isort .
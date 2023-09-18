run:
	docker-compose build && docker-compose up -d

down:
	docker-compose down

upgrade-db:
	docker exec q_bot alembic upgrade head

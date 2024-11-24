check:  # Type annotation validation, code formatting, and error detection.
	@if docker ps -q -f name=trello-pet-project; then \
		docker exec -it trello-pet-project /bin/bash -c "mypy . && black --line-length 80 . && flake8 . && pylint ."; \
	elif docker compose ps -q; then \
		docker compose up --build -d && \
		docker compose exec app pylint . && \
		docker compose exec app mypy . && \
		docker compose exec app black --line-length 80 . && \
		docker compose exec app flake8 . && \
		docker compose down; \
	else \
		mypy . && black --line-length 80 . && flake8 . && pylint .; \
	fi

DOCKER_COMPOSE := $(shell which docker-compose || which docker)

start:	# Launching the docker
	docker compose up --build

test:	# Running tests
	pytest tests/

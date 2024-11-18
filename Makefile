flake8_pylint_ruff:
	flake8 create_companies/ && \
	flake8 tests/ && \
	pylint create_companies/ && \
	pylint tests/ && ruff check .    # Launch the linters

black:
	black --line-length 80 .        # Black is the uncompromising Python code formatter.

DOCKER_COMPOSE := $(shell which docker-compose || which docker)

start:
ifeq ($(DOCKER_COMPOSE),/usr/local/bin/docker-compose)
	@echo "Using docker-compose"
	docker-compose up --build
else
	@echo "Using docker compose"
	docker compose up --build
endif

test:
	pytest tests/

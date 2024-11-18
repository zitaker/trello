black_flake8_pylint_ruff:
	black --line-length 80 . && \
	flake8 src/ && \
	pylint src/ && \
	ruff check src/		# Code formatter and error detection.


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

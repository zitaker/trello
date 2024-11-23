mypy_black_flake8_pylint:	# Type annotation validation, code formatting, and error detection.
	mypy src/ && \
	black --line-length 80 src/ && \
	flake8 src/ && \
	pylint src/


DOCKER_COMPOSE := $(shell which docker-compose || which docker)

start:	# Launching the docker
ifeq ($(DOCKER_COMPOSE),/usr/local/bin/docker-compose)
	@echo "Using docker-compose"
	docker-compose up --build
else
	@echo "Using docker compose"
	docker compose up --build
endif

test:	# Running tests
	pytest tests/

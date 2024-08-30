flake8_pylint:
	flake8 src/ flake8 tests/ & pylint src/ & pylint tests/    # Launch the linters

black:
	black --line-length 80 .        # Black is the uncompromising Python code formatter.

start:
	docker-compose up --build

test:
	pytest tests/       # Running tests.


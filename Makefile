.PHONY: lint
lint:
	ruff check .
	mypy .

.PHONY: format
format:
	ruff check . --fix
	ruff format .

.PHONY: test
test:
	pytest --cov=. --cov-report=term-missing
.PHONY: lint
lint:
	ruff check .
	mypy .
	bandit -r src

.PHONY: format
format:
	ruff check . --fix
	ruff format .

.PHONY: test
test:
	pytest --cov=. --cov-report=term-missing

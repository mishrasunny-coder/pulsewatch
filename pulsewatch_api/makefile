.PHONY: dev test lint type ci

dev:
	uv run uvicorn pulsewatch_api.main:app --reload --port 8000

test:
	uv run pytest

lint:
	uv run ruff check .

type:
	uv run mypy src

ci: lint type test

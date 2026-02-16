.PHONY: test lint format clean check-clean help

test:
	uv run pytest tests/ -v

lint:
	uv run flake8 model

format:
	uv run isort model tests
	uv run black model tests

clean:
	rm -rf build/ dist/ *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

check-clean:
	@if [ -n "$$(git status --porcelain)" ]; then \
		echo "Found uncommitted changes:"; \
		git status --porcelain; \
		exit 1; \
	else \
		echo "Working directory is clean."; \
	fi

help:
	@echo "Available commands:"
	@echo "  test              Run tests with pytest"
	@echo "  lint              Run fast lint checks"
	@echo "  format            Format code with isort and black"
	@echo "  clean             Clean build artifacts"
	@echo "  check-clean       Check no uncommitted changes"
	@echo "  help              Show this help message"

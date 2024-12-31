# Variable for Poetry (helps reuse in commands)
POETRY = poetry

# Variable for the test filter (optional)
FILTER ?=

# Install project dependencies
install:
	$(POETRY) install --no-root

# Main target to run tests
test:
	@if [ "$(FILTER)" ]; then \
		echo "Running tests filtered by pattern: $(FILTER)"; \
		pytest -k $(FILTER) --durations=0 -v; \
	else \
		echo "Running all tests"; \
		pytest --durations=0 -v; \
	fi

# Target to watch for test changes
test-watch:
	@if [ "$(FILTER)" ]; then \
		echo "Watching tests filtered by pattern: $(FILTER)"; \
		ptw -- -k $(FILTER) --durations=0 -v; \
	else \
		echo "Watching all tests"; \
		ptw -- --durations=0 -v; \
	fi

# Check code with Flake8 and Isort
lint:
	$(POETRY) run flake8 .
	$(POETRY) run isort --check . src

# Format code with Black and Isort
format:
	$(POETRY) run black .
	$(POETRY) run isort . src

# Update dependencies to their latest versions
update:
	$(POETRY) update

# Clean temporary files and caches
clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .coverage
	rm -rf *.egg-info

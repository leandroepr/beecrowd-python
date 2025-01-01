# Variable for Poetry (helps reuse in commands)
POETRY = poetry

# Variable for the test filter (optional)
FILTER ?=

# Install project dependencies
install:
	$(POETRY) lock --no-update
	$(POETRY) install --no-root

# Main target to run tests (all or filtered by the FILTER variable)
test:
	@if [ "$(FILTER)" ]; then \
		echo "Running tests filtered by pattern: $(FILTER)"; \
		$(POETRY) run pytest -k $(FILTER) --durations=0 -v; \
	else \
		echo "Running all tests"; \
		$(POETRY) run pytest --durations=0 -v; \
	fi

# Target to watch for test changes (all or filtered by the FILTER variable)
test-watch:
	@if [ "$(FILTER)" ]; then \
		echo "Watching tests filtered by pattern: $(FILTER)"; \
		$(POETRY) run sh -c 'ptw -- --durations=0 -v -k "$(FILTER)"'; \
	else \
		echo "Watching all tests"; \
		$(POETRY) run sh -c 'ptw -- --durations=0 -v'; \
	fi

# Lint code using Flake8 and Isort
lint:
	$(POETRY) run flake8 .
	$(POETRY) run isort --check .

# Format code using Black and Isort
format:
	$(POETRY) run black .
	$(POETRY) run isort .

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

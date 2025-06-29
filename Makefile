.PHONY: ci lint tests docs

# 1. Lint & type-check
lint:
	black --check .
	flake8 .
	mypy .

# 2. Tests + coverage
tests:
	pytest --cov=leetcode_playground --cov-report=term-missing

# 3. Generar docs
docs:
	@sphinx-build -M html docs docs/_build

# 4. Pipeline completo
ci: lint tests docs


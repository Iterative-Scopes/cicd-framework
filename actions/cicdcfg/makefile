PYTHON_VERSION = 3.9
VENV = .py$(PYTHON_VERSION)
PYTHON = python3
BIN = $(VENV)/bin
PACKAGE_NAME = mloperator
PACKAGE_DIST = $(shell find dist -type f -execdir basename '{}' ';')

help: ## show commands
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

venv: ## setup virtual enviroment and install depedencies
venv: setup.py
	$(PYTHON) -m venv $(VENV)
	$(BIN)/python --version
# install runtime and development requirments
	$(BIN)/pip install -e .

build: ## create a release
build: setup.py src/cicdcfg/*.py
	$(BIN)/python setup.py sdist


clean: ##clean venv and cached files
clean:
	rm -rf .pytest_cache
	rm -rf .tox
	rm -rf src/*.egg*
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete


VENV_PATH ?= .venv
VENV_REQUIREMENTS = $(VENV_PATH)/.timestamp
PIP_REQUIREMENTS = $(VENV_PATH)/.requirements-timestamp
DEV_REQUIREMENTS = $(VENV_PATH)/.dev-requirements-timestamp
DOC_REQUIREMENTS = $(VENV_PATH)/.doc-requirements-timestamp
TEST_REQUIREMENTS = $(VENV_PATH)/.test-requirements-timestamp
VENV_BIN = $(VENV_PATH)/bin
PIP_COMMAND = pip3
PYTHON_PATH = $(shell which python3)
PYTHON_VERSION = $(shell printf '%b' "import sys\nprint(f'{sys.version_info.major}.{sys.version_info.minor}')" | $$(which python3))
PINNED_DEPS ?= reqs.txt

# ********************
# Variable definitions
# ********************

# Package name
PACKAGE = ili2py
LOCATION ?= ./src

# Python source files
SRC_PY = $(shell find $(LOCATION)/$(PACKAGE) -name '*.py')

# Environment variables used for build
BUILD_ENV += \
	DEVELOPMENT=${DEVELOPMENT}

# *******************
# Set up environments
# *******************

$(VENV_REQUIREMENTS):
	$(PYTHON_PATH) -m venv $(VENV_PATH)
	touch $@

$(PIP_REQUIREMENTS): $(VENV_REQUIREMENTS) pyproject.toml
	$(VENV_BIN)/$(PIP_COMMAND) install --upgrade pip wheel setuptools
	$(VENV_BIN)/$(PIP_COMMAND) install .
	touch $@

$(DOC_REQUIREMENTS): $(PIP_REQUIREMENTS)
	$(VENV_BIN)/$(PIP_COMMAND) install .[docs]
	touch $@

$(DEV_REQUIREMENTS): $(PIP_REQUIREMENTS)
	$(VENV_BIN)/$(PIP_COMMAND) install -e .[dev]
	touch $@

$(TEST_REQUIREMENTS): $(PIP_REQUIREMENTS)
	$(VENV_BIN)/$(PIP_COMMAND) install -e .[test]
	touch $@

# **************
# Common targets
# **************

# Build dependencies
BUILD_DEPS += $(PIP_REQUIREMENTS)

.PHONY: install
install: $(PIP_REQUIREMENTS)

.PHONY: install-docs
install-docs: $(PIP_REQUIREMENTS) $(DOC_REQUIREMENTS)

.PHONY: install-dev
install-dev: $(PIP_REQUIREMENTS) $(DEV_REQUIREMENTS)

.PHONY: install-dev
install-test: $(PIP_REQUIREMENTS) $(DEV_REQUIREMENTS) $(TEST_REQUIREMENTS)

.PHONY: build
build: $(BUILD_DEPS)
	$(VENV_BIN)/python setup.py bdist_wheel

.PHONY: clean
clean:
	find ./src -name "*.pyc" -delete

.PHONY: clean-all
clean-all: clean
	rm -rf $(VENV_PATH)
	rm -rf src/$(PACKAGE).egg-info
	rm -rf docs/site
	rm -rf build
	rm -rf dist

.PHONY: git-attributes
git-attributes:
	git --no-pager diff --check `git log --oneline | tail -1 | cut --fields=1 --delimiter=' '`

.PHONY: dev
dev: setup.py install-dev
	$(VENV_BIN)/pip install -e .

.PHONY: test-coverage
test-coverage: $(TEST_REQUIREMENTS) $(VARS_FILES) install-dev
	$(VENV_BIN)/py.test -vv --cov-config .coveragerc --cov $(PACKAGE) --cov-report term-missing:skip-covered tests

.PHONY: test
test: $(TEST_REQUIREMENTS) $(VARS_FILES) install-dev
	$(VENV_BIN)/py.test -vv tests

.PHONY: tests
tests: test

.PHONY: check
check: $(PIP_REQUIREMENTS) $(TEST_REQUIREMENTS)
	mypy --explicit-package-bases --show-error-codes src/$(PACKAGE) tests

.PHONY: doc-html
doc-html: $(DOC_REQUIREMENTS) docs/mkdocs.yml
	rm -rf doc/site
	$(VENV_BIN)/mkdocs build -f docs/mkdocs.yml -d site

.PHONY: doc-serve
doc-serve: $(DOC_REQUIREMENTS) docs/mkdocs.yml
	$(VENV_BIN)/mkdocs serve -f docs/mkdocs.yml

.PHONY: updates
updates: $(PIP_REQUIREMENTS)
	$(VENV_BIN)/pip list --outdated

.PHONY: pin-deps
pin-deps: $(PIP_REQUIREMENTS) $(TEST_REQUIREMENTS)
	pip freeze --all > $(PINNED_DEPS)

.PHONY: binary
binary: $(PIP_REQUIREMENTS) $(DEV_REQUIREMENTS)
	$(VENV_BIN)/pyinstaller --name ili2py --onefile --noconfirm \
		--add-data "src/ili2py:ili2py" \
		src/ili2py/cli.py

.PHONY: output-test
output-test: $(PIP_REQUIREMENTS) $(DEV_REQUIREMENTS)
	$(VENV_BIN)/python src/ili2py/scripts/generate_test_output.py
	find build/ili2py_output_test/mermaid/ -type f -name "*.md" | parallel -j 4 'mmdc -i {} -o {.}.png --puppeteerConfigFile=puppeteer-config.json'
	plantuml -tpng build/ili2py_output_test/plantuml/*.puml
	zip -r build/ili2py_output_test.zip  build/ili2py_output_test

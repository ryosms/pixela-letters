.PHONY: build publish publish-test

# ==================== publish ====================

build:
	@poetry build

publish:
	@poetry publish

publish-test:
	@poetry publish -r testpypi

# ==================== test ====================

.PHONY: test

test:
	@poetry run pytest

# ==================== linter ====================
SOURCE_DIR:=pixela_letters tests

.PHONY: fix black isort flake8

fix: black isort flake8

black:
	@poetry run black ${SOURCE_DIR}

isort:
	@poetry run isort ${SOURCE_DIR}

flake8:
	@poetry run pflake8 ${SOURCE_DIR}


.PHONY: check check-black check-isort

check: check-black check-isort flake8

check-black:
	@poetry run black --check ${SOURCE_DIR}

check-isort:
	@poetry run isort --check ${SOURCE_DIR}


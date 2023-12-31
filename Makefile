gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall dist/*.whl

lint:
	poetry run flake8 gendiff tests

install:
	poetry install

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

local-test-coverage:
	poetry run pytest --cov=gendiff
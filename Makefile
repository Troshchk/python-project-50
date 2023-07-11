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
	poetry run flake8 brain_games

install:
	poetry install
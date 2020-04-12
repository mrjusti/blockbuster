#   ___ _
#   /   (_) __ _ _ __   __ _  ___
#  / /\ / |/ _` | '_ \ / _` |/ _ \
# / /_//| | (_| | | | | (_| | (_) |
#/___,'_/ |\__,_|_| |_|\__, |\___/
#     |__/             |___/

.PHONY: build run lint tests clean-pyc clean-build

PROJECT := "django"
HOST=127.0.0.1
TEST_PATH=./

clean-pyc:
	find . -name '*.pyc' -exec rm -rf {} +
	find . -name '*.pyo' -exec rm -rf {} +

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

build:
	poetry install
	poetry run python blockbuster/manage.py migrate

run:
	poetry run python blockbuster/manage.py runserver

lint:
	poetry run flake8
	poetry run mypy blockbuster
	poetry run bento check --all

test: clean-pyc
	poetry run pytest --verbose --color=yes $(TEST_PATH)
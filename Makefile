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
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	name '*~' -exec rm --force  {}

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

build:
	poetry install
	poetry run python blockbuster/manage.py migrate

run:
	poetry run python blockbuster/manage.py runserver

lint:
	poetry run flake8 --exclude=.tox
	poetry run mypy blockbuster
	poetry run bento check --all

test: clean-pyc
    poetry py.test --verbose --color=yes $(TEST_PATH)
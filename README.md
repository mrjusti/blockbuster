manage dependencies

https://python-poetry.org/

# install
poetry install
poetry run python blockbuster/manage.py migrate

# run server
poetry run python blockbuster/manage.py runserver



// To Do
- [ ] try and catch
- [ ] middleware proper message and http status handler
- [ ] tests infrastructure
- [ ] tests acceptance
- [X] PEP8
- [X] lint
- [X] Makefile
- [ ] typed collections for movies list and people
- [ ] write the README.md and explain what I did
- [ ] shared type
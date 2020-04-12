manage dependencies

https://python-poetry.org/

# install
poetry install
poetry run python blockbuster/manage.py migrate

# run server
poetry run python blockbuster/manage.py runserver



// To Do
- [X] try and catch
- [X] middleware proper message and http status handler
- [X] tests infrastructure
- [X] tests acceptance
- [X] PEP8
- [X] lint
- [X] Makefile
- [ ] typed collections for movies list and people
- [ ] write the README.md and explain what I did
- [ ] shared type
- [X] improve acceptance test and infrastructure
- [ ] coverage
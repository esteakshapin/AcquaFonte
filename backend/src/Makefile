.PHONY: clean
clean:
	rm *~

.PHONY: test
test:
	. venv/bin/activate && python manage.py test

.PHONY: coverage
coverage:
	. ../venv/bin/activate && coverage run --source='.' --omit="venv/*" manage.py test
	. ../venv/bin/activate && coverage html
	. ../venv/bin/activate && coverage report -m

.PHONY: flake8
flake8:
	flake8 . --exclude=*/migrations/*,venv/,manage.py,assets/

.PHONY: freeze
freeze:
	pip freeze > requirements.txt

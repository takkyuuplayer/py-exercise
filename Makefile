test:
	pipenv run python -m unittest discover -s tests -p "*.py"

install:
	pipenv install

run:
	@cd docker && $(MAKE) run

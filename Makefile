all: setup

setup:
	pipenv install --three

test:
	pipenv run python -m unittest discover -s tests -p "*.py"

run:
	@$(MAKE) -C docker run

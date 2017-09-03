test:
	python -m unittest discover -s tests -p "*.py"

run:
	@cd docker && $(MAKE) run

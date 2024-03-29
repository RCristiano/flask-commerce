.PHONY: help run coverage clean requirements poetry

help:
	@echo "    run"
	@echo "        Run the project."
	@echo "    coverage"
	@echo "        Run the project coverage."
	@echo "    clean"
	@echo "        Remove cache files."
	@echo "    requirements"
	@echo "        Update requirements.txt file."

poetry:
	@poetry install

requirements: poetry;
	@poetry export -f requirements.txt -o requirements.txt

run: poetry;
	@poetry run flask run -h '0.0.0.0' -p 5000

coverage:
	@coverage run
	@coverage report
	@coverage html
	@coverage xml

clean:
	@find . -name '__pycache__'  -exec rm -rf {} +
	@find . -name '*coverage*' -exec rm -rf {} +
	@find . -name '*.sqlite' -exec rm -rf {} +
	@rm -rf htmlcov
	@rm -f cov.xml

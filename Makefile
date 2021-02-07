.PHONY: requirements coverage

coverage:
	coverage run
	coverage report
	coverage html

requirements:
	poetry export -f requirements.txt --output requirements.txt

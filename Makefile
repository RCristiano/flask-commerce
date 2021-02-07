.PHONY: requirements coverage clean

coverage:
	@coverage run
	@coverage report
	@coverage html
	@coverage xml

heroku:
	@poetry export -E heroku -f requirements.txt --output requirements.txt

clean:
	@find . -name '__pycache__'  -exec rm -rf {} +
	@find . -name '*coverage*' -exec rm -rf {} +
	@find . -name '*.sqlite' -exec rm -rf {} +
	@rm -rf htmlcov
	@rm -f cov.xml

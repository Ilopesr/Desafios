test:
	pytest -v

pack:
	pip install -e .

lint:
	pre-commit run --all-files

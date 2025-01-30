test:
	pytest -v

pack:
	pip install -e .

requirements:
	poetry export --without-hashes --without-urls | awk '{ print $1 }' FS=';' > requirements.txt

lint:
	pre-commit run --all-files

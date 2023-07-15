build_local:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

test_local:
	python -m unittest tests/health.py
	python -m unittest tests/convert.py

scan_local:
	pip-audit -r ./requirements.txt

deploy:
	sh docker.sh
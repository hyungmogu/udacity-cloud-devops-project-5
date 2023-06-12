run_kompose:
	kompose convert -f docker-compose.yml

audit_local:
	pip-audit -r ./requirements.txt

build_local:
	pip install -r requirements.txt

test_local:
	python -m unittest tests/services/convert.py

start:
	docker-compose build server &&\
	docker-compose up server 
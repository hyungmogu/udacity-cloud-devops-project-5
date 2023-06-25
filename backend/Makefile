venv/bin/activate:
	python3 -m venv ./venv &&\
	./venv/bin/pip install python-dotenv==1.0.0

run_kompose:
	kompose convert -f docker-compose.yml

build_local:
	pip install -r requirements.txt

prepare_kubernetes:
	python ./prepare_kubernetes.py

setup_local:
	sh ./setup.sh

start_minikube venv/bin/activate:
	sh ./minikube.sh

start_audit:
	docker-compose build audit &&\
	docker-compose up audit

start_load_test:
	docker-compose build load-test &&\
	docker-compose up load-test

start_unit_test:
	docker-compose build unit-test &&\
	docker-compose up unit-test

start:
	docker-compose build server &&\
	docker-compose up server 
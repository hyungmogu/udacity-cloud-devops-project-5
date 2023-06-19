run_kompose:
	kompose convert -f docker-compose.yml

audit_local:
	pip-audit -r ./requirements.txt

build_local:
	pip install -r requirements.txt

setup_local:
	sh ./setup.sh

start_minikube:
	sh ./minikube.sh

start_load_test:
	docker-compose build server &&\
	docker-compose up load-test

start_unit_test:
	docker-compose build server &&\
	docker-compose up unit-test

start:
	docker-compose build server &&\
	docker-compose up server 
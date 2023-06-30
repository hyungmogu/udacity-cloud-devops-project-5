run_kompose:
	kompose convert -f docker-compose.yml

build_local:
	pip install -r requirements.txt

prepare_kubernetes:
	python ./prepare_kubernetes.py

prepare_docker:
	sh ./docker.sh

setup_local:
	sh ./setup.sh

clear_minikube:
	minikube delete --all

start_minikube_dashboard:
	minikube dashboard

start_minikube:
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
	sh start.sh
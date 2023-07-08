start_microservices_minikube:
	minikube start && \
	kubectl apply -f ./.circleci/kubernetes/base_src/ &&\
	kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml &&\
	minikube service gateway-service

prepare_microservices_minikube:
	python3 -m venv ./venv &&\
	./venv/bin/pip install python-dotenv==1.0.0 &&\
	./venv/bin/python3 ./prepare_kubernetes.py

start_microservices:
	docker-compose build &&\
	docker-compose up

prepare_microservices:
	python3 -m venv ./venv &&\
	./venv/bin/pip install python-dotenv==1.0.0 &&\
	./venv/bin/python3 ./prepare_docker.py

setup_local:
	cp .env.example .env;

start_local: prepare_microservices start_microservices

start_local_minikube: prepare_microservices_minikube start_microservices_minikube
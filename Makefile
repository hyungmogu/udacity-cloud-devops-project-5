start_microservices_minikube:
	minikube start && \
	kubectl apply -f ./.circleci/kubernetes/base_src/ &&\
	kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml &&\
	minikube service gateway-service

prepare_microservices_minikube:
	python3 -m venv ./venv &&\
	./venv/bin/pip install python-dotenv==1.0.0 &&\
	./venv/bin/python3 ./prepare_docker.py &&\
	./venv/bin/python3 ./prepare_kubernetes.py

clean_microservices_minikube:
	minikube delete --all

prepare_microservices:
	python3 -m venv ./venv &&\
	./venv/bin/pip install python-dotenv==1.0.0 &&\
	./venv/bin/python3 ./prepare_docker.py

start_locust:
	locust -f tests/load/locustfile.py -P 8089

setup_local:
	cp .env.example .env;

test_integration_microservices: clean_microservices_minikube prepare_microservices_minikube start_microservices_minikube
	./venv/bin/pip install requests==2.31.0 &&\
	./venv/bin/pip install Pillow==9.5.0 &&\
	./venv/bin/pip install boto3==1.26.148 &&\
	./venv/bin/pip install python-dotenv==1.0.0 &&\
	./venv/bin/python3 -m pytest -s -v tests/integration_microservices

test_load_local: start_locust clean_microservices_minikube prepare_microservices_minikube start_microservices_minikube

start_minikube_dashboard:
	minikube dashboard

start_minikube: clean_microservices_minikube prepare_microservices_minikube start_microservices_minikube
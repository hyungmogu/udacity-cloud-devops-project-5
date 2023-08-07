install_dependencies:
	python3 -m venv ./venv &&\
	./venv/bin/pip install python-dotenv==1.0.0 &&\
	./venv/bin/pip install requests==2.31.0 &&\
	./venv/bin/pip install Pillow==9.5.0 &&\
	./venv/bin/pip install boto3==1.26.148 &&\
	./venv/bin/pip install moto==4.1.11 &&\
	./venv/bin/pip install locust==2.16.1

prepare_minikube:
	./venv/bin/python3 ./prepare_docker.py &&\
	./venv/bin/python3 ./prepare_kubernetes.py

start_locust:
	locust -f tests/load/locustfile.py -P 8089

test_integration_microservices: install_dependencies clean_minikube prepare_minikube start_minikube
	./venv/bin/python3 -m pytest -s -v tests/integration_microservices

test_load: install_dependencies start_locust clean_minikube prepare_minikube start_minikube

start_minikube_dashboard:
	minikube dashboard

clean_minikube:
	minikube delete --all

start_minikube: install_dependencies clean_minikube prepare_minikube
	minikube start --vm-driver=docker --kubernetes-version=v1.27.0 && \
	kubectl apply -f ./.circleci/kubernetes/base_src/ &&\
	kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml &&\
	minikube service gateway-service --url

setup_minikube:
	cp .env.example .env;
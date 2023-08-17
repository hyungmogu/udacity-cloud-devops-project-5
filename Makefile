install_dependencies:
	python3 -m venv ./venv &&\
	./venv/bin/pip install -r requirements.txt

prepare_kubernetes:
	./venv/bin/python3 ./prepare_kubernetes.py

prepare_minikube:
	./venv/bin/python3 ./prepare_docker.py &&\
	./venv/bin/python3 ./prepare_kubernetes.py

start_locust:
	locust -f tests/load/locustfile.py -P 8089

test_integration_microservices: install_dependencies clean_minikube prepare_minikube start_minikube
	./venv/bin/python3 -m pytest -s -v tests/integration_microservices

test_unit: install_dependencies prepare_minikube
	# for each microservice folder, go into it and run command `make test`
	CURRENT_DIR=`pwd` &&\
	echo $$CURRENT_DIR &&\
	for dir in $$(find microservices -maxdepth 1 -type d); do\
		if [ $$dir != "." ]; then\
			cd $$CURRENT_DIR/$$dir &&\
			pwd &&\
			make clear &&\
			make build &&\
			make test &&\
			cd $$CURRENT_DIR;\
		fi;\
	done

test_load: install_dependencies start_locust clean_minikube prepare_minikube start_minikube

start_minikube_dashboard:
	minikube dashboard

clean_minikube:
	minikube delete --all

start_minikube: install_dependencies clean_minikube prepare_minikube
	minikube start &&\
	sh deploy_dockers.sh &&\
	kubectl apply -f ./.circleci/kubernetes/local_namespaces_src/ &&\
	kubectl apply -f ./.circleci/kubernetes/local_base_redis_src/ &&\
	kubectl apply -f ./.circleci/kubernetes/prod_namespaces_src/ &&\
	kubectl apply -f ./.circleci/kubernetes/prod_base_src/ &&\
	kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml &&\
	sh setup_redis_cluster.sh &&\
	minikube service gateway-service -n image-converter-main --url

setup_minikube:
	cp .env.example .env;
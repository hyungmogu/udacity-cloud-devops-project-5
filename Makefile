start_microservices:
	docker-compose build &&\
	docker-compose up

prepare_microservices:
	python3 -m venv ./venv &&\
	./venv/bin/pip install python-dotenv==1.0.0 &&\
	./venv/bin/python3 ./prepare_docker.py

start_frontend:
	cd frontend &&\
	make start;

setup_local:
	cp .env.example .env;

start_local: prepare_microservices start_microservices start_frontend

stop_local: stop_backend stop_frontend



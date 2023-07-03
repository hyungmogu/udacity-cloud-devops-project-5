start_backend:
	cd microservices/server &&\
	make start;

start_frontend:
	cd frontend &&\
	make start;

start_local: start_backend start_frontend

stop_local: stop_backend stop_frontend



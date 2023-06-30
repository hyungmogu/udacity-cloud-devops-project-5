start_backend:
	cd backend &&\
	sh start.sh;

start_frontend:
	cd frontend &&\
	sh start.sh;

start_local: start_backend start_frontend

stop_local: stop_backend stop_frontend



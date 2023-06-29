start_backend:
  cd backend &&\
  make start

start_local: start_backend start_frontend

stop_local: stop_backend stop_frontend



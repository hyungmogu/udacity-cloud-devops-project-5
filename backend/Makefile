run_kompose:
	kompose convert -f docker-compose.yml

build_local:
	pip install -r requirements.txt

start:
	docker-compose build server &&\
	docker-compose up server 
lint:
	hadolint Dockerfile
	./venv/bin/python3 -m pylint --rcfile=.pylintrc --disable=R,C,W1203,W1202 ./**/**.py

clear:
	rm -rf venv

build:
	python3 -m venv venv &&\
	./venv/bin/pip install -r requirements.txt

test:
	./venv/bin/python3 -m unittest discover

scan:
	./venv/bin/python3 -m pip_audit -r ./requirements.txt

deploy:
	sh deploy.sh
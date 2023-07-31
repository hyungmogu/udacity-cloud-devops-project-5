lint_local:
	hadolint Dockerfile
	./venv/bin/python3 -m pylint --disable=R,C,W1203,W1202 ./**/**.py

build_local:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

test_local:
	./venv/bin/python3 -m unittest discover

scan_local:
	./venv/bin/python3 -m pip_audit -r ./requirements.txt

deploy:
	sh deploy.sh
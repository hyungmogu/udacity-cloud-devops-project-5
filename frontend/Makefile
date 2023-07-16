scan_local:
	npm install &&\
    npm audit --audit-level=critical

build_local:
	echo "Building locally" &&\
	npm install &&\
	npm run build;
	
test_local:
	echo "Running tests locally" &&\
	npm run test:unit;

start:
	npm install &&\
	npm run dev;

stop:
	pass
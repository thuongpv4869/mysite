#!/bin/bash

if [ "$1" == "ctn" ]; then
	if [ "$2" == "up" ]; then
		python manage.py runserver 0.0.0.0:8000
	fi
fi

if [ "$1" == "up" ]; then
	docker-compose up -d

elif [ "$1" == "build" ]; then
	export DOCKER_BUILDKIT=1
	docker-compose build --progress=plain

elif [ "$1" == "fmt" ]; then
	autopep8 -r -i .
	
elif [ "$1" == "lint" ]; then
	pre-commit run --all-files

elif [ "$1" == "fze" ]; then
	docker exec mysite_web_1 pipenv requirements > requirements/prod.txt
	docker exec mysite_web_1 pipenv requirements --dev > requirements/local.txt

elif [ "$1" == "bash" ]; then
	docker exec -it mysite_web_1 bash
fi
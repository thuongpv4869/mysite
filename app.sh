#!/bin/bash

is_django_running () {
	if docker ps --format '{{.Names}}' | grep -w mysite_django_1 &> /dev/null; then
    	return 0
	fi
	return 1
}

if [ "$1" == "up" ]; then
	docker-compose up django
	exit
fi

if [ "$1" == "setup-devtool" ]; then
	pip install autopep8
	pip install pre-commit
	exit
fi

if [ "$1" == "build" ]; then
	export DOCKER_BUILDKIT=1
	docker-compose build --progress=plain
	exit
fi

if [ "$1" == "fmt" ]; then
	autopep8 -r -i .
	exit
fi
	
if [ "$1" == "lint" ]; then
	pre-commit run --all-files
	exit
fi

if [ "$1" == "bash" ]; then
	if is_django_running; then
    	docker-compose exec django bash
	else
		docker-compose run django bash
	fi
	exit
fi

if [ "$1" == "test" ]; then
	if is_django_running; then
    	docker-compose exec django python manage.py test
	else
		docker-compose run django python manage.py test
	fi
	exit
fi
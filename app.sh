#!/bin/bash

if [ "$1" == "up" ]; then
	python manage.py runserver

elif [ "$1" == "fmt" ]; then
	autopep8 -r -i .
	
elif [ "$1" == "lint" ]; then
	pre-commit run --all-files
fi
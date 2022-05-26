#!/bin/bash

if [ "$1"=="up" ]; then
	python manage.py runserver
fi
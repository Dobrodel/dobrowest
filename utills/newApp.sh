#!/bin/bash

if [ -z "$1" ] 
then
	echo "Please get me name's application"
else
	python manage.py startapp "$1"
fi

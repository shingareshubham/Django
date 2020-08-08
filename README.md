# Repo contains Django Projects..


# Django Bsic Commands:

## Create project
> django-admin startproject project_name

## Create App
> python manage.py startapp app_name

## Run server
> python manage.py runserver

## Load all static folders i.e. css, js, images
> python manage.py collectstatic

## make migration
> python manage.py makemigrations

## to Add specific migration
> python manage.py sqlmigrate app_name 0001

## Migrate all
> python manage.py migrate

## Create superuser for admin panel
> python manage.py createsuperuser


# Requirement
## for connecting db to django install connector
> pip install psycog2

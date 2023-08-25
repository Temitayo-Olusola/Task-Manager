# Project Overview
  This is a task manager app built in python which utilizes the Djangorestframework to execute CRUD functionalities.

#Pre Requisites
  Python 3.10
  Django 4.2.4

#Installation
  http://github.com/Temitayo-Olusola/Task-Manager.git
  cd Task

#Dependencies
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py runserver

#API endpoints
  127.0.0.1/api/taskapp - create new task, delete task, update a task, retrieve tasks and list all tasks.

#Test
  python manage.py test taskapp

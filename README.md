#Project Overview -
  A Task manager application built in Django which uses the integration of the djangorestframework to enable CRUD functionality.

#Installation -
  git clone https://github.com/Temitayo-Olusola/Task-Manager.git

#dependencies - 
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py runserver

#API Endpoints -
  http://127.0.0.1/api/taskapp - Create a task, List all tasks.
  http://127.0.0.1/api/taskapp/task.id  - Delete a task, Retrieve a task, and Update a task

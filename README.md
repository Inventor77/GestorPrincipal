# GESTOR PRINCIPAL

##### _TO MANAGE LEADS IN SPAIN, YOU'D SAY "GESTOR PRINCIPAL"_

### What it does

**GESTOR PRINCIPAL** is a web app that allows users

### How I built it

###### Project Setup

Install the **_pipenv_** using pip and virtual environment is set using `pipenv shell` command which will create a _pipfile_.
After that install **_django_** (python backend framework), **_django rest framework_** (creates api) and **_django rest knox_** (token authentication) using `pipenv install django djangorestframework django-rest-knox`.
Created Django project named _GestorPrincipal_ using `django-admin startproject GestorPrincipal`.
After that created the Django App named _guias_ using `python3 manage.py startapp guias`. And configured guias app in setting.py file inside Main app (GestorPrincipal) folder by adding 'guias.apps.GuiasAppConfig' in INSTALLED_APPS array.
After this created the model(inside models.py file of guias app) which will be in class form , class named as Guias and defined the field in class for name(CharField), email(EmailField), message(CharField) and created_date(DateTimeField).
Then created the migration using `python3 manage.py makemigrations guias` and to add it to database `python3 manage.py migrate`

###### API Creation

From Django Rest Framework, **_Serializer_** have been used to convert the model instances to Native Python Datatypes which will be easily rendered into JSON. After this new file named api.py is created and used **_Viewset_** to create CRUD API without specifying the explicit methods using created serializer and setup the urls.py file in guias app.



#### What's next for GESTOR PRINCIPAL

### Built With

`Python3` `Django` `Django Rest Framework` `Django Rest Knox`

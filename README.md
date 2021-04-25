# GESTOR PRINCIPAL

##### _TO MANAGE LEADS IN SPAIN, YOU'D SAY "GESTOR PRINCIPAL"_

### What it does

**GESTOR PRINCIPAL** is a web app that allows users

### How I built it

###### Project Setup

Install the **_pipenv_** using pip and virtual environment is set using `pipenv shell` command which will create a _pipfile_.
After that install **_django_** (python backend framework), **_django rest framework_** (creates api) and **_django rest knox_** (token authentication) using `pipenv install django djangorestframework django-rest-knox`.
Created Django project named _GestorPrincipal_ using `django-admin startproject GestorPrincipal`.
After that created the Django App named _guias_ using `python3 manage.py startapp guias`. And configured guias app in setting.py file inside Main app (GestorPrincipal) folder by adding 'guias.apps.GuiasAppConfig' in INSTALLED*APPS array.
After this created the model(inside models.py file of guias app) which will be in class form , class named as Guias and defined the field in class for name(CharField), email(EmailField), message(CharField) and created_date(DateTimeField).
Then created the migration using `python3 manage.py makemigrations guias` and to add it to database `python3 manage.py migrate`
Created a **.gitignore** file and add \_node_module* on top and go to gitignore.io type django and add this content to .gitignore file.

###### API Creation

From Django Rest Framework, **_Serializer_** have been used to convert the model instances to Native Python Datatypes which will be easily rendered into JSON. After this new file named api.py is created and used **_Viewset_** to create CRUD API without specifying the explicit methods using created serializer and setup the urls.py file in guias app.

###### Setting Up React

Created the app named frontend and configure this app in setting.py file of Main App. Create other directories src and components inside src folder using `mkdir -p ./frontend/src/components`. Also create static and templates folder with frontend folder inside both of them using `mkdir -p ./frontend/{static, templates}/frontend`. Create package.json file using `npm init -y` to include all javascript dependencies. Install the **_WebPack_** and **_WebPack-cli_** using `npm i -D webpack webpack-cli`. Next thing is install **_babel_** to transpile javascript using `npm i -D @babel/core babel-loader @babel/preset-env @babel/preset-react babel-plugin-transform-class-properties`. when webpack is used then babel loader is needed to transpile code, for each version of js presets are required here preset-env transpile ES2015+ (for respective preset we can use preset-es2015, preset-es2016 ....) and also react-preset. Here babel plugin transform-class-properties is handling static class properties for es2015 es2016 and so. Install **_React_** , **_react-dom_** and **_prop-types_** using `npm i react react-dom prop-types`. In order to use presets and plugin file .babelrc is created and list down the presets and plugins in json format. Create webpack.config.js file and load the babel loader.
Add following code in package.json

```
"dev": "webpack --mode development ./GestorPrincipal/frontend/src/index.js --output-path ./GestorPrincipal/frontend/static/frontend/main.js",
"build": "webpack --mode production ./GestorPrincipal/frontend/src/index.js --output-path ./GestorPrincipal/frontend/static/frontend/main.js"
```

Create a index.js file in frontend/src, this file loads the main App component of react. After this run `npm run dev`.

#### What's next for GESTOR PRINCIPAL

### Built With

`Python3` `Django` `Django Rest Framework` `Django Rest Knox`
`React` `React Router`
`Webpack` `Babel` 

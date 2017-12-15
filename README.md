# Gift site is made by Django, Python, Sqlite

## Introduction
Gift site is developed by __Django__. Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Django has an authentication framework which allows user's to login into the the application easily. In this project __user authentication__ is done by user email and password authentication. __Bootstrap__ is used to make it responsive and __Paypal__ payment process is developed by __django-paypal__ to any transaction of products. 

## Structure
The Gift site has one main project is called Gift. __Gift__ project has three Apps called __products__, __user_account__ and __paypal_store__. 

![structure](https://user-images.githubusercontent.com/24476948/34054674-eaabcdd0-e1c3-11e7-88ac-95328db6db09.png)



## Main steps to develop the project
1.__Create Project__
To start to develop site we need to install python and django in our device by using this comment below:
``` 
python --version
```
```
easy_install --version
```
```
easy_install django
```
Now using django-admin we create our Gift project.
```
django-admin startproject Gift
```
Then we got those file in Gift project:
* __manage.py__: Perfoms admin tasks for our project, such as putting it on the system path, or starting the built-in webserver.
* __settings.py__: This is the settings file for your project, where you define your project’s configuration settings, including database connections, other applications, templates, and more.
* __urls.py__: The url declarations for this Django project. This file contains a list of mappings which connect urls to views.
* __wsgi.py__: An entry-point for WSGI-compatible web servers to serve our project. This file handles our requests/responses to/from Django development server.
* ____init__ __.py__: An empty file that informs Python that this directory should be considered a Python package.

   

## Content

## Technology stack

## Instructions

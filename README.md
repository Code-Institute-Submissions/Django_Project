# Gift site is made by Django, Python, Sqlite

## Introduction
Gift site is developed by __Django__. Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Django has an authentication framework which allows user's to login into the the application easily. In this project __user authentication__ is done by user email and password authentication. __Bootstrap__ is used to make it responsive and __Paypal__ payment process is developed by __django-paypal__ to any transaction of products. 

## Structure
The Gift site has one main project is called Gift. __Gift__ project has three Apps called __products__, __user_account__ and __paypal_store__. 
* __products:__ This app contains all the product categories and products details.
* __user_account:__ By using this app user can register, login and logout from the site.
* __paypal_store:__ This app includes all the payments transaction on site.
* __media:__ This includes all images and video file needed for the site.
* __requriments.txt:__ In this text file all the dependency need for the project.


![structure](https://user-images.githubusercontent.com/24476948/34054674-eaabcdd0-e1c3-11e7-88ac-95328db6db09.png)



## Main steps to develop the project
1. __Create Project:__
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
* __init.py__: An empty file that informs Python that this directory should be considered a Python package.

 2. __Create App:__ 
 To create the app we need to use this comment below:
 ```
 django-admin start app products
 ```
 ```
 django-admin start app user_account
 ```
 ```
 django-admin start app paypal_store
 ```
After doinig this we need to Update the INSTALLED_APPS in your settings.py file:

![sett](https://user-images.githubusercontent.com/24476948/34059391-c6571c2e-e1d6-11e7-99bb-6555d9d2c47c.png)

3.__Create Super User:__ 
To manage the admin section we need to create a super user in our site. By using below comment in terminal a super user can create:
```
python manage.py createsuperuser
```


## Content
### 1)products App
All the products for the site is developed in products app. The products app is include those file like migrations, static, templates,__init.py__,  admin.py, apps.py, models.py, tests.py, views.py and urls.py.

![product2](https://user-images.githubusercontent.com/24476948/34073338-712453ca-e28f-11e7-99c1-3a9a9579d540.png)

* __models.py:__ A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data storing. Each model maps to a single database table. There are two class is created for Product and Category to store in database. Then we apply below comment in terminal:
```
python manage.py makemigrations 
```
```
python manage.py migrate
```

* __admin.py:__ 
To get the all Product and Category in our admin site we need to add this in admin.py:
```
from django.contrib import admin
from .models import Category, Product
```
```
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
```
* __urls.py:__
The url tag helps us to generate links in the templates.At this point urls.py file in products app looks like this:

![urls1](https://user-images.githubusercontent.com/24476948/34073548-f7393008-e293-11e7-81b3-81862c02b3c6.png)

* __views.py:__
Django has the concept of views to encapsulate the logic responsible for processing a user’s request and for returning the response.Add a view function to views.py is connect to our urls.py and show the html pages from the templates.
```
from django.shortcuts import render, get_object_or_404
from .models import Product, Category

```
* __get_object_or_404()__ This pattern is so common that [Django](https://www.djangoproject.com/start/overview/) a provides a shortcurt method called [get_object_or_404()](https://overiq.com/django/1.10/showing-404-errors-in-django). To use get_object_or_404() method with models, queryset and managers. It also shows that when a matching record is not found, get_object_or_404() raises Http404 exception.
* __render()__
To combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.Django does not provide a shortcut function which returns a TemplateResponse because the constructor of TemplateResponse offers the same level of convenience as [render()](https://docs.djangoproject.com/en/2.0/topics/http/shortcuts/).
```
return render(request, "products/products_view/product_list.html",
 {"products": products,"category":category,"categories":categories})
```
* __templates:__
The [template](https://docs.djangoproject.com/en/2.0/topics/templates/) layer provides a designer-friendly syntax for rendering the information to be presented to the user. In products templates contains html file like base.html, index.html, product_details.html and product_list.html page. First we have to setup templates in setting.py file like:
```

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
1. __base.html:__
It contains basic the structure for the hole site and all other pages are shown in this page.
```
 {% block content %}
       {% endblock %}
```
2. __index.html:__
The index page is home page for the site.
![index](https://user-images.githubusercontent.com/24476948/34073875-e1c6246c-e29b-11e7-925e-c31a62eafc46.png)

3. __product_list.html:__
All the products and categories are show in this page:
![product_list](https://user-images.githubusercontent.com/24476948/34073913-9c688788-e29c-11e7-9ee6-6d50dfe704fc.png)

4. __product_details.html:__
Every product details is shown when we click on More About Product button on product list page.
![prduct_detail](https://user-images.githubusercontent.com/24476948/34073942-4718382c-e29d-11e7-9b26-0e3bb0042c54.png)

5. __static:__
It contains the css file and javascript file needed for the site. First we need to setup the static file in setting.py
```
STATIC_URL = '/static/'
STARICFILES_DIRS = (os.path.join(BASE_DIR, 'products/static'))
```
* __custom.css__: It has all custom  css code for the site. 

### 2)user_account app:
User can easily to create an account in this Gift site.Django has an authentication framework which allows user's to login into the the application easily. User_account app is to develop for user registration, login and logout in the Gift site.The authentication framework is implemented as 'django.contrib.auth' app but it is also depends upon on 'django.contrib.contenttype' app and some middlewares.
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products',
    'paypal.standard.ipn',
    'paypal_store',
    'django_forms_bootstrap',
    'user_account',

]
```
Django authentication also uses session behind the scenes. As a result, you must have the following two middlewares in the MIDDLEWARE list in settings.py.
```

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',    
]
```
We also need to add this our setting.py file:
```
AUTH_USER_MODEL = 'user_account.User'
```
To use authentication system you must have 'django.contrib.auth' and 'django.contrib.contenttype' in the INSTALLED_APPS list as follows:
User_account app include thoes files migrations,templates,__init.py__, admin.py, apps.py, models.py, tests.py, views.py,forms.py, backends.py and urls.py.
* __models.py:__
The User model is considered as heart of Django authentication. To use User model you must first import it from django.contrib.auth.models.
```
from django.contrib.auth.models import AbstractUser, UserManager
```
* __views.py:__
In user_account app views are developed for the register, login, logout and profile.
* __forms.py:__
The syntax of creating forms in Django is almost similar to that of creating models, the only differences are Django form inherits from __forms.Form__ instead of __models.Model__. and each form fields inherits __forms.FieldName__ instead of __models.FieldName__. The user_account has registration form and login form:
```
class UserRegistrationForm(UserCreationForm)
class UserLoginForm(forms.Form)
```
* __backends.py:__
we need to modify our settings.py so that Django knows to use this backend instead of the system default
```
AUTHENTICATION_BACKENDS = (
   'django.contrib.auth.backends.ModelBackend',
    'user_account.backends.EmailAuth',
)

```
Here we’ve created a class that will replace the standard ‘auth’ object that Django uses to check logins, and we override two of its default methods. The authenticate method is where we are doing the main logic by finding the user by the email address and then checking password.
* __urls.py:__
we have been hardcoding URLs in our templates.If we want to update the URL structure we have manually visit each and every templates to update the URL. This problem can be solved easily by using url tag in our templates. user_account urls.py include those

![urls2](https://user-images.githubusercontent.com/24476948/34129606-9de3aa74-e43c-11e7-962c-ee9f9166a7a2.png)
* __templates:__
user_account app templates contains register.thml, login.html and profile.html file.
1. __register.html:__
By using New User page any one can register on this site.

![register](https://user-images.githubusercontent.com/24476948/34109691-4d6e56f6-e3fc-11e7-8cec-ce7837e69ea3.png)

2. __login.html:__
User can login in ths site by using this page:

![log_in](https://user-images.githubusercontent.com/24476948/34109680-48dab3a0-e3fc-11e7-9c67-504d10fd924f.png)



## Technology stack
1. __Django:__
[Django](https://www.djangoproject.com/start/overview/) takes care of much of the hassle of Web development.  Django takes care of user authentication, content administration, site maps, RSS feeds, and many more tasks. This site develop by those django task given below
   * __[Django Models](https://docs.djangoproject.com/en/2.0/topics/db/models/):__
   Each model is a Python class that subclasses __django.db.models.Model__. Each attribute of the model represents a database field. With all of this, Django gives you an automatically-generated database-access API.
   * __[Django Views](https://docs.djangoproject.com/en/2.0/topics/http/views/):__
   A view function, or view for short, is simply a Python function that takes a Web request and returns a Web response. This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image or anything. The view itself contains whatever arbitrary logic is necessary to return that response.
   * __[Templates](https://docs.djangoproject.com/en/2.0/topics/templates/):__
   The Django template language is Django’s own template system. Until Django 1.8 it was the only built-in option available.
   * __[Django Admin](https://docs.djangoproject.com/en/2.0/ref/contrib/admin/):__
   One of the most powerful parts of Django is the automatic admin interface. It reads metadata from your models to provide a quick, model-centric interface where trusted users can manage content on your site. The admin’s recommended use is limited to an organization’s internal management tool. It’s not intended for building your entire front end around.
   * __[Django Form](https://docs.djangoproject.com/en/2.0/topics/forms/)__
   Django handles three distinct parts of the work involved in forms. It preparing and restructuring data to make it ready for rendering, creating HTML forms for the data and receiving and processing submitted forms and data from the client.
   * __[Django User authentication ](https://docs.djangoproject.com/en/2.0/topics/auth/):___
   Django comes with a user authentication system. It handles user accounts, groups, permissions and cookie-based user sessions. Django authentication system handles both authentication and authorization.
   
2. __[Python](https://www.python.org/):__
Python is a widely used high-level programming language for general-purpose programming.Python interpreters are available for many operating systems.
3. __[Paypal]( http://developer.paypal.com):__
PayPal offers safe and secure payments, without the need for special security methods on the developer’s part or the website hosting platform, to ensure that the customer’s details are safe.
4. __[Bootstrap](https://getbootstrap.com/):__
Bootstrap. Build responsive, mobile-first projects on the web with the world's most popular front-end component library. Bootstrap is an open source toolkit for developing with HTML, CSS, and JS. 
5. __HTML:__
6. __CSS:__


## Instructions
Open your terminal and use the git clone command:

git clone https://github.com/hureferdous/Django_Project.git

Once the project is cloned, enter in Gift directory:

cd Gift

It's recommended to use a virtual environment (to keep isolated the dependencies required by this project). If you don't have it installed, you can do it using pip pip install virtualenv.

Here you have the instructions: [Virtual Environment - The Hitchhiker's Guide to Python] (http://docs.python-guide.org/en/latest/dev/virtualenvs/)

Create a virtual environment for this project and activate it.

Install the dependencies:

pip install -r requirements.txt

To do that, open your terminal and run 
```
 python manage.py makemigrations
```
```
 python manage.py migrate
```
```
 python manage.py runserver
```
Now you can open up your browser and in the URL bar enter http://127.0.0.1:8000

# Stochastic Blog Core API 

Core Django APIS for life-is-stochastic blog [webapp](https://lifeisstochastic.netlify.app/ "webapp").

Production version is currently hosted at [heroku](https://stochastic-core.herokuapp.com/ "heroku").

## Installation

	$ conda create -n stochastic-core
	$ conda activate stochastic-core
	$ pip install -r requirements.txt


## Set the necessary Environment Variables

Set all the below mentioned environement variables on your activate.d and deactivate.d file of your **stochastic-core** environment. More information at conda documentation [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#setting-environment-variables "here") to guide you through the process.

set SECRET_KEY=
set DATABASE_NAME==
set DATABASE_USER=
set DATABASE_PASSWORD=
set DATABASE_HOST=
set DATABASE_PORT=

## Run migrations

	$ python manage.py makemigrations
	$ python manage.py migrate
	
## Start the server
	$ python manage.py runserver


## Stochastic API DOCS

RETRIEVE: /blog/{id}/

GET: /blog

POST: /blog/
```
    {
    	"blog_title": "this is title",
    	"blog_content": "<h1> Hello world</h1>",
    	"author": "Gaurav Adhikari",
    	"category": "Tech"
    }
```

PUT: /blog/
```
    {
    	"blog_title": "this is title2",
    	"blog_content": "<h1> Hello world</h1>",
    	"author": "Gaurav Adhikari",
    	"category": "Tech"
    }
```

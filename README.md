# manotes-api

A Python restful-api sample.

[![Coverage Status](https://coveralls.io/repos/github/antunesleo/manotes-api/badge.svg?branch=master)](https://coveralls.io/github/antunesleo/manotes-api?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/42b0f620dec82226efb2/maintainability)](https://codeclimate.com/github/antunesleo/manotes-api/maintainability)
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
If you prefer, you can also use Docker to get your copy running.

## Local Installation

### Prerequisites

* Linux
* Python 3+
* Pip3
* Virtualenvwrapper (optional but recommended)
* PostgreSQL 10+ 

### Installing

Installing requirements
```
$ sudo apt-get install redis-server
$ git clone git@github.com:antunesleo/manotes-api.git
$ mkvirtualenv manotes-api (Optional)
$ workon manotes-api (Optional)
$ pip install -r requirements.txt
$ pip install -r requirements_dev.txt
```
Dealing with environments variables

```
$ cd
$ vim .bashrc

Add this in the end of file and reopen the terminal
alias load-env='export $(cat .env | xargs)'
alias load-env-test='export $(cat .env.test | xargs)'

$ load-env
```

Setting up database
```
$ sudo apt-get install postgres
$ sudo su postgres
$ psql
$ CREATE ROLE manotes SUPERUSER LOGIN PASSWORD 'manotes'
$ CREATE DATABASE manotes
$ ALTER DATABASE manotes OWNER TO manotes;
$ \q
$ exit

Create a .env file based on .env.sample, with your custom configuration (if necessary) and then:
$ load-env
$ python manage.py db upgrade

```

Configuring tests coverage
```
sudo vim .coveralls.yml

repo_token: <repo_token>
service_name: manotes
```

#### Running the tests
```
load-env-test
python -m testtools.run
```

#### Updating testing-coverage
```
coverage run --omit=<path_to_envs>/* -m testtools.run
coveralls
```

#### Running API - Local Installation
```
load-env
python run.py
```

## Docker

### Installing

Preparing the Environment Variables

```bash
$ cp .env.sample.docker .env
$ cp .env.postgres.sample .env
```

You can also copy using your file browser, if you prefer.

Change the default configurations, as **TEMP_FILE_PATH** or **TEMP_PATH** to your project home path.

```bash
$ docker-compose up --build -d
$ docker-compose exec web bash
# python manage.py db upgrade
```

The last command will run the migrations

*This will also take your project running!*

### Running tests

```bash
$ docker-compose up -d
$ docker-copose exec web bash
```

This will take you inside the Web Container Bash.

```bash
$ python -m testtools.run
```

### Updating tests coverage
```bash
$ docker-compose up -d
$ docker-compose exec web bash
```

This will take you inside the Web Container Bash.

```bash
coverage run --omit=<path_to_envs>/* -m testtools.run
coveralls
```

### Running API
```bash
$ docker-compose up -d
```

## Features
| Features        | Description   |
| -------------   |:-------------:| 
| Login | [POST] in 'api/login' endpoint, unauthenticated users can login |
| Create Account  | [POST] in endpoint 'api/users' users can create account passing email, username and password| 
| Update Account  | [PUT] in endpoint 'api/users' authenticated users can update account infos like email and/or username| 
| Update Avatar   | [PUT] in endpoint 'api/users/me/avatar' authenticated users can update avatar passing an image file|
| Create Note     | [POST] in endpoint 'api/users/me/notes' authenticated user can create a note with name, content and color |
| Update Note     | [PUT] in endpoint 'api/users/me/notes' authenticated user can update name, content and color from a note|
| Get Note        | [GET] in endpoint 'api/users/me/notes/<note_id>' authenticated user can list all notes or get a specific note if note_id is passed |
| Delete Note     | [DELETE] in endpoint 'api/users/me/notes/<note_id>' authenticated user can delete a note |


## Built With

* [Alembic](http://alembic.zzzcomputing.com/en/latest/) - lightweight database migration tool for usage with the SQLAlchemy Database Toolkit
* [boto3](https://pypi.org/project/boto3/) - AWS SDK for Python, which allows Python developers to write software that makes use of services like S3.
* [celery](https://pypi.org/project/celery/) - Distributed task queue
* [coveralls](https://pypi.org/project/python-coveralls/) - Python interface to coveralls.io API
* [coverage](https://pypi.org/project/coverage/) - Code coverage measurement for Python
* [Flask](http://flask.pocoo.org/) - The web framework used
* [flask-CORS](https://flask-cors.readthedocs.io/en/latest/) - A Flask extension for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible.
* [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/) - an extension that handles SQLAlchemy database migrations for Flask applications using Alembic.
* [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/) - an extension for Flask that adds support for quickly building REST APIs
* [gunicorn](https://pypi.org/search/?q=gunicorn) - a Python WSGI HTTP Server for UNIX
* [mock](https://pypi.org/project/mock/) - mock is a library for testing in Python. It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.
* [passlib](https://pypi.org/project/passlib/) - comprehensive password hashing framework
* [pip](https://pypi.org/project/pip/) - Dependency Management
* [Psycopg](http://initd.org/psycopg/) - PostgreSQL adapter for the Python programming language
* [SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL toolkit and Object Relational Mapper
* [SQLAlchemy-Utils](https://pypi.org/project/SQLAlchemy-Utils/) - Various utility functions for SQLAlchemy.
* [testtools](http://testtools.readthedocs.io/en/latest/for-test-authors.html) - testtools is a set of extensions to Python’s standard unittest module.

## Authors

* **Leonardo Antunes** - *Initial work* - [antunesleo](https://github.com/antunesleo)
* **Pedro Pozzi Ferreira** - *Dockerization and Packages Update* - [PozziSan](https://github.com/PozziSan)


See also the list of [contributors](https://github.com/antunesleo/manotes-api/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

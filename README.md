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
* Virtual Env (optional but recommended)
* PostgreSQL 10+ 

### Installing

Installing requirements
```
$ sudo apt-get install redis-server
$ git clone git@github.com:antunesleo/manotes-api.git
$ python3 -m venv manotes-api (optional)
$ source manotes-api/bin/activate (optional)
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

Create test database:
```
$ sudo su postgres
$ psql
$ CREATE DATABASE manotes_test
$ ALTER DATABASE manotes_test OWNER TO manotes;
$ \q
$ exit
```

Run them all:
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


## Contributors

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/antunesleo">
        <img src="https://avatars0.githubusercontent.com/u/13929952?s=400&u=8c46ff05e5295aa7f085f5ec8aeddf5af6bc4677&v=4" width="100px;" alt=""/>
        <br />
        <sub>
          <b>Leonardo Antunes</b>
          <span> - Lead Development</span>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/PozziSan">
        <img src="https://avatars2.githubusercontent.com/u/22599880?s=400&u=14ef80f14c4e6dae753dc7e88a065e4e608c3c83&v=4" width="100px;" alt=""/>
        <br />
        <sub>
          <b>Pedro Pozzi Ferreira</b>
          <span> - Dockerization and Packages Update </span>
        </sub>
      </a>
    </td>
  </tr>
</table>  


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

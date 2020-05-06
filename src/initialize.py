# -*- coding: utf-8 -*-
import datetime
from flask import Flask, g, request
from flask_sqlalchemy import SQLAlchemy
from src import database, config as config_module
from src.async_tasks import establish


config = config_module.get_config()
web_app = Flask(__name__)
web_app.config.from_object(config)

establish.make_worker(web_app)
worker = establish.worker
establish.register_tasks(worker)

database.AppActiveRepository.db = SQLAlchemy(web_app)


# TODO: Precisa refatorar os testes
@web_app.before_request
def before_request():
    from src.security import authentication
    token = request.cookies.get('userToken')
    encoded_token = request.cookies.get('userEncodedToken')
    user_email = request.cookies.get('userEmail')

    authentication.AuthService.check_authorization(user_email, encoded_token)


@web_app.after_request
def add_token_header(response):
    user = g.get("user")
    if user is not None:
        token = g.current_token
        expire_date = datetime.datetime.now()
        expire_date = expire_date + datetime.timedelta(days=90)
        response.set_cookie('userToken', token, expires=expire_date)
        response.set_cookie('userEncodedToken', g.encoded_token, expires=expire_date)
        response.set_cookie('userEmail', g.user.email, expires=expire_date)
    return response


def create_api():
    from src import api
    api.create_api(web_app)


create_api()


def run():
    web_app.run(host=str(config.APP_BASE_URL), port=int(config.PORT), debug=True, threaded=True)

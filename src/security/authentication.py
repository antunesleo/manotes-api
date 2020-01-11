# -*- coding: utf-8 -*-
from flask import g
from src import exceptions
from src.security import security_services


class AuthService(object):

    @classmethod
    def authenticate_with_credentials(cls, credentials):
        from src.house import residents
        username_or_email = credentials['username_or_email']
        try:
            if security_services.ValidationService.is_email(username_or_email):
                user = residents.User.create_with_email(username_or_email)
            else:
                user = residents.User.create_with_username(username_or_email)
        except exceptions.NotFound:
            raise exceptions.UserNotExists('Could not find a user with username {}'.format(username_or_email))

        return security_services.HashService.is_string_equals_to_hash(credentials['password'], user.password), user

    @classmethod
    def authenticate_with_token(cls, token):
        from src.house import residents
        try:
            user = residents.User.create_with_token(token)
            g.user = user
            g.current_token = user.token
            g.authenticated = True
        except exceptions.NotFound:
            g.authenticated = False

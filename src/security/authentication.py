# -*- coding: utf-8 -*-
from flask import g
from src import exceptions
from src.base.services import DomainService
from src.security import security_services
from src.house.services import ResidentsService


class AuthService(DomainService):

    @classmethod
    def authenticate_with_credentials(cls, credentials):
        user_factory = ResidentsService.pass_me_the_user_factory()
        username_or_email = credentials['username_or_email']
        try:
            if security_services.ValidationService.is_email(username_or_email):
                user = user_factory.create_with_email(username_or_email)
            else:
                user = user_factory.create_with_username(username_or_email)
            encoded_token = security_services.EncodingService.encode(user.as_dict(full=True), user.token)
            user.encoded_token = encoded_token
        except exceptions.NotFound:
            raise exceptions.UserNotExists('Could not find a user with username {}'.format(username_or_email))
        return security_services.HashService.is_string_equals_to_hash(credentials['password'], user.password), user

    @classmethod
    def check_authorization(cls, user_email, encoded_token):
        try:
            user_class = ResidentsService.pass_me_the_user_factory()
            user = user_class.create_with_email(user_email)
        except exceptions.NotFound:
            g.authenticated = False
            return

        try:
            user_dict = security_services.EncodingService.decode(encoded_token, user.token)
            user = user_class.create_with_dict(user_dict)
            g.user = user
            g.current_token = user.token
            g.encoded_token = encoded_token
            g.authenticated = True
        except exceptions.DecodingError:
            g.authenticated = False

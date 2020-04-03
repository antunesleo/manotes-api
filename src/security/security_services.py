# -*- coding: utf-8 -*-
import secrets

import jwt

from src.base.services import InfraService
from passlib.hash import pbkdf2_sha256
from validate_email import validate_email


class HashService(InfraService):

    @classmethod
    def hash(cls, word):
        return pbkdf2_sha256.hash(word)

    @classmethod
    def is_string_equals_to_hash(cls, string, hashed_string):
        return pbkdf2_sha256.verify(string, hashed_string)


class TokenService(InfraService):

    @classmethod
    def generate(cls, size=40):
        return secrets.token_hex(size)


class ValidationService(InfraService):

    @classmethod
    def is_email(cls, email):
        return validate_email(email)


class EncodingService(InfraService):

    @classmethod
    def encode(cls, dict_to_encode, secret):
        return jwt.encode(dict_to_encode, secret, algorithm='HS256')

    @classmethod
    def decode(cls, dict_to_decode, secret):
        return jwt.decode(dict_to_decode, secret, algorithm='HS256')

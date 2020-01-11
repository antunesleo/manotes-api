# -*- coding: utf-8 -*-
import secrets
from src.base.services import Service
from passlib.hash import pbkdf2_sha256
from validate_email import validate_email


class HashService(Service):

    @classmethod
    def hash(cls, word):
        return pbkdf2_sha256.hash(word)

    @classmethod
    def is_string_equals_to_hash(cls, string, hashed_string):
        return pbkdf2_sha256.verify(string, hashed_string)


class TokenService(Service):

    @classmethod
    def generate(cls, size=40):
        return secrets.token_hex(size)


class ValidationService(Service):

    @classmethod
    def is_email(cls, email):
        return validate_email(email)

# -*- coding: utf-8 -*-
import secrets

import jwt

from src.base.services import InfraService
from passlib.hash import pbkdf2_sha256
from validate_email import validate_email
from src import exceptions


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
        try:
            return jwt.decode(dict_to_decode, secret, algorithm='HS256')
        except jwt.InvalidSignatureError:
            raise exceptions.DecodingError('Could not decode because the key is invalid')
        except jwt.DecodeError:
            raise exceptions.DecodingError('Could not decode because the token is invalid')
        except Exception:
            raise exceptions.DecodingError('Could not decode.')

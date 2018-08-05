# -*- coding: utf-8 -*-
import datetime
from app import config as config_module
from app import database, exceptions

db = database.AppRepository.db

config = config_module.get_config()


class AlreadyExist(Exception):
    pass


class NotExist(Exception):
    pass


class RepositoryError(Exception):
    pass


class EmailAlreadyExists(Exception):
    pass


class UsernameAlreadyExists(Exception):
    pass


class AbstractModel(object):

    @classmethod
    def one_or_none(cls, **kwargs):
        return cls.filter(**kwargs).one_or_none()

    @classmethod
    def filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs)

    def save_db(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        else:
            db.session.flush()

    def delete_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def create_from_json(cls, json_data):
        try:
            instance = cls()
            instance.set_values(json_data)
            instance.save_db()
            return instance
        except Exception as ex:
            raise RepositoryError(str(ex))

    def update_from_json(self, json_data):
        try:
            self.set_values(json_data)
            self.save_db()
            return self
        except Exception as ex:
            raise RepositoryError(str(ex))

    def set_values(self, json_data):
        for key, value in json_data.items():
            setattr(self, key, json_data.get(key, getattr(self, key))) # WTF


class User(db.Model, AbstractModel):
    __tablename__ = 'manotes_users'
    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    token = db.Column(db.String)
    password = db.Column(db.String)

    @classmethod
    def create_from_json(cls, json_data):
        try:
            instance = cls()
            instance.set_values(json_data)
            instance.save_db()
            return instance
        except Exception as ex:
            if 'manotes_users_email_key' in str(ex):
                raise exceptions.EmailAlreadyExists('Could not create user because the email already exists')
            if 'manotes_users_username_key' in str(ex):
                raise exceptions.UsernameAlreadyExists('Could not create user because the username already exists')
            raise RepositoryError(str(ex))

    def update_from_json(self, json_data):
        try:
            self.set_values(json_data)
            self.save_db()
            return self
        except Exception as ex:
            if 'manotes_user_email_key' in str(ex):
                raise exceptions.EmailAlreadyExists('Could not update user because the email already exists')
            if 'manotes_user_username_key' in str(ex):
                raise exceptions.UsernameAlreadyExists('Could not update user because the username already exists')
            raise RepositoryError(str(ex))


class Note(db.Model, AbstractModel):
    __tablename__ = 'manotes_notes'
    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('manotes_users.id'), nullable=False)
    name = db.Column(db.String)
    content = db.Column(db.String)
    color = db.Column(db.String)
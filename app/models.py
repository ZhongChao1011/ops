#!/usr/bin/env python
# -*- coding: utf8 -*-

'''
Created on 2017/12/18
@author: ChaoZhong
@email: 16796679@qq.com
'''

import datetime
from uuid import uuid1
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager


class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), unique=True, nullable=False)

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __unicode__(self):
        return self.username


class Hosts(db.Model):
    __tablename__ = 'hosts'
    __searchable__ = ['hostname', 'wip', 'iip']
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(100), unique=True, nullable=False)
    wip = db.Column(db.String(100), unique=True, nullable=False)
    iip = db.Column(db.String(100), unique=True, nullable=False)
    idc = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.datetime.now())
    cat_id = db.Column(db.String(100), db.ForeignKey('category.id'))

    def __unicode__(self):
        return '<Host %s>' % self.hostname


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.String(100), primary_key=True, default=str(uuid1()))
    cat_name = db.Column(db.String(100), unique=True, nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.datetime.now())
    hosts = db.relationship('Hosts', backref='category', lazy='dynamic')

    def __unicode__(self):
        return '<Category %s>' % self.cat_name


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

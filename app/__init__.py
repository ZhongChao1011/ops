#!/usr/bin/env python
# -*- coding: utf8 -*-

'''
Created on 2017/12/18
@author: ChaoZhong
@email: 16796679@qq.com
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.session_protection = 'strong'


from . import views
from .models import Users, Hosts, Category
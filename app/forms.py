#!/usr/bin/env python
# -*- coding: utf8 -*-

'''
Created on 2017/12/18
@author: ChaoZhong
@email: 16796679@qq.com
'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, IPAddress
from .models import Category

class UsersForm(FlaskForm):
    """登录表单"""
    username = StringField(u'用户名', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired(), Length(min=6, message=u'密码长度不对')])
    submit = SubmitField(u'登 录')


class HostAddForm(FlaskForm):
    hostname = StringField(u'主机名', validators=[DataRequired(), Length(min=-1, max=100, message=u'主机名最大长度100')])
    wip = StringField(u'外网', validators=[DataRequired(), IPAddress])
    iip = StringField(u'内网', validators=[DataRequired(), IPAddress])
    idc = StringField(u'IDC', validators=[DataRequired(), Length(min=-1, max=50)])
    category = SelectField(u'项目', choices=[(cat.id, cat.cat_name)
                                           for cat in Category.query.order_by(Category.cat_name).all()])
    submit = SubmitField(u'添加')


class CatAddForm(FlaskForm):
    cat_name = StringField('项目名称', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField(u'添加')



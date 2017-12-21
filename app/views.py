#!/usr/bin/env python
# -*- coding: utf8 -*-

'''
Created on 2017/12/18
@author: ChaoZhong
@email: 16796679@qq.com
'''

from sqlalchemy import or_
from flask import request, render_template, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user
from . import app, db
from .models import Users, Hosts, Category
from .forms import UsersForm, HostAddForm, CatAddForm
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# 主页视图
@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')


# 登录视图
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = UsersForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = Users.query.filter_by(username=form.username.data).first()
            if user is not None and user.verify_password(form.password.data):
                login_user(user)
                flash('欢迎 %s 回来!' % form.username.data, 'info')
                return redirect(request.args.get('next') or url_for('index'))
            flash(u'无效的用户名或密码', 'Danger')
    return render_template('login.html', form=form)


# 退出登录视图
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u'你已退出Gemstone Ops!', 'warning')
    return redirect(url_for('login'))


# 主机管理视图
@app.route('/host_manage', methods=['GET', 'POST'])
@login_required
def host_manage():
    page = request.args.get('page', 1, type=int)
    q = request.args.get('q', None)
    form = HostAddForm()
    if q is not None:
        pagination = Hosts.query.filter(
            or_(
                Hosts.hostname.like("%"+q+"%"),
                Hosts.wip.like("%"+q+"%"),
                Hosts.iip.like("%"+q+"%")
            )
        ).paginate(
            page,
            per_page=10,
            error_out=False)
        hosts = pagination.items
        return render_template('host_manage.html', hosts=hosts, form=form, pagination=pagination)

    pagination = Hosts.query.order_by('start_time').paginate(
        page,
        per_page=10,
        error_out=False
    )
    hosts = pagination.items

    if request.method == 'POST':
        if form.validate_on_submit():
            add_host = Hosts(
                hostname=form.hostname.data,
                wip=form.wip.data,
                iip=form.iip.data,
                cat_id=form.category.data,
                idc=form.idc.data)
            db.session.add(add_host)
            db.session.commit()
            flash(u'主机 %s 添加成功!' % unicode(form.hostname.data), 'success')
        return redirect(request.args.get('next') or url_for('host_manage'))

    return render_template('host_manage.html', hosts=hosts, form=form, pagination=pagination)



# 项目管理视图
@app.route('/cat_manage', methods=['GET', 'POST'])
@login_required
def cat_manage():
    cats = Category.query.order_by('cat_name').all()
    form = CatAddForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            cat = Category.query.filter_by(cat_name=form.cat_name.data).first()
            if cat is None:
                add_cat = Category(cat_name=form.cat_name.data)
                db.session.add(add_cat)
                db.session.commit()
                flash(u'添加 %s 成功' % unicode(form.cat_name.data), 'success')
                return redirect(request.args.get('next') or url_for('cat_manage'))
            else:
                flash(u'项目已存在!', 'Danger')
                return redirect(request.args.get('next') or url_for('cat_manage'))
    return render_template('cat_manage.html', form=form, cats=cats)
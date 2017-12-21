#!/usr/bin/env python
# -*- coding: utf8 -*-

'''
Created on 2017/12/18
@author: ChaoZhong
@email: 16796679@qq.com
'''

from flask_script import Manager, Server, Shell
from flask_migrate import Migrate, MigrateCommand
from app import app
from app import db

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('runserver', Server())
manager.add_command('shell', Shell())
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
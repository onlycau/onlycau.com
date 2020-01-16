#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

'''
Deployment toolkit.
'''

import os, re

from datetime import datetime

from fabric.tasks import task 
from fabric import Config, Connection

c_remote = Connection(host='106.12.58.231',
    user='root',
    port=19945,
    connect_kwargs={'password':'982074165x*'})
    

db_user = 'web_user'
db_password = '020202'

_TAR_FILE = 'dist-www.tar.gz'

_REMOTE_TMP_TAR = '/tmp/%s' % _TAR_FILE

_REMOTE_BASE_DIR = '/www-data/'

def _current_path():
    return os.path.abspath('.')

def _now():
    return datetime.now().strftime('%y-%m-%d_%H.%M.%S')


@task
def backup(c):
    '''
    Dump entire database on server and backup to local.
    '''
    dt = _now()
    f = 'backup-www-%s.sql' % dt
    c_remote.open()
    with c_remote.cd('/tmp'):
        c_remote.run('mysqldump --user=%s --password=%s --skip-opt --add-drop-table --default-character-set=utf8 --quick web > %s' % (db_user, db_password, f))
        c_remote.run('tar -czvf %s.tar.gz %s' % (f, f))
        c_remote.get('/tmp/%s.tar.gz' % f, '/tmp/ %s.tar.gz' % f)
        c_remote.run('rm -f %s' % f)
        c_remote.run('rm -f %s.tar.gz' % f)

@task
def build(c):
    '''
    Build dist package.
    '''
    includes = ['static', '*.py']
    excludes = ['test', '.*', '*.pyc', '*.pyo']
    with c.cd(os.path.join(_current_path(), 'www')):
        c.run('rm -f dist/%s' % _TAR_FILE)
        cmd = ['tar', '--dereference', '-czvf', '../%s' % _TAR_FILE]
        cmd.extend(['--exclude=\'%s\'' % ex for ex in excludes])
        cmd.extend(includes)
        c.run(' '.join(cmd))

@task
def deploy(c):
    newdir = 'back-%s' % _now()
    c_remote.open()
    c_remote.put('%s' % _TAR_FILE, _REMOTE_TMP_TAR)
    with c_remote.cd(_REMOTE_BASE_DIR):
        c_remote.run('mkdir %s' % newdir)
    with c_remote.cd('%s/%s' % (_REMOTE_BASE_DIR, newdir)):
        c_remote.run('tar -xzvf %s' % _REMOTE_TMP_TAR)
    with c_remote.cd(_REMOTE_BASE_DIR):
        c_remote.run('rm -f www')
        c_remote.run('ln -s %s www' % newdir)
        c_remote.run('chown www-data:www-data www')
        c_remote.run('chown -R www-data:www-data %s' % newdir)
        c_remote.run('supervisorctl stop awesome')
        c_remote.run('supervisorctl start awesome')
        c_remote.run('/etc/init.d/nginx reload')
"""
gunicorn WSGI multiprocess server configuration.
https://luis-sena.medium.com/gunicorn-worker-types-youre-probably-using-them-wrong-381239e13594
https://docs.gunicorn.org/en/latest/configure.html
"""
import multiprocessing
import os

default_proc_name = 'python-gunicorn-multiprocess'
chdir = './app'
bind = '0.0.0.0:' + os.environ.get('PORT', '8000')
disable_redirect_access_to_syslog = True
reload = True

if os.environ.get('APP_ENV') == "production":
    worker_class = 'gthread'
    workers = multiprocessing.cpu_count() * 2 + 1
    reload = False

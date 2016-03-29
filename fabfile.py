# -*- coding: utf-8 -*-

# stolen from https://github.com/chroto/flaskplate
# http://docs.fabfile.org/en/1.5/tutorial.html
from contextlib import contextmanager

from fabric.api import local, cd, prefix, env
import os


BASE_DIR = os.path.join(os.path.dirname(__file__))
ENV_DIR = os.path.join(BASE_DIR, 'env')

PROJECT = "shanemartin"
activate = os.path.join(BASE_DIR, 'env', 'bin', 'activate')


@contextmanager
def virtualenv():
    with prefix('. {activate}'.format(activate=activate)):
        yield


def setup(environ='dev'):
    """
    Setup virtual env and python packages.
    """
    requirements = os.path.join(
        BASE_DIR, 'requirements', '{}.txt'.format(environ))

    local("virtualenv env")
    with virtualenv():
        local("pip install -r {}".format(requirements))


def run():
    """
    Runs the application in development mode.
    """
    with virtualenv():
        local("python manage.py server")


def freeze():
    with virtualenv():
        local("python freeze.py")

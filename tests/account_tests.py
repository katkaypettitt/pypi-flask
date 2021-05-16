# More tests would be needed before deployment

from flask import Response
from pypi_org.data.users import User
from pypi_org.viewmodels.account.register_viewmodel import RegisterViewModel
from pypi_org.views.account_views import register_post
from tests.test_client import flask_app
import unittest.mock


def test_register_validation_when_valid():
    form_data = {
        'name': 'Kat',
        'email': 'katrinakay.alaimo@gmail.com',
        'password': 'kat'*3
    }

    with flask_app.test_request_context(path='/account/register', data=form_data):
        vm = RegisterViewModel()

    # Avoids database call on register
    target = 'pypi_org.services.user_service.find_user_by_email'
    with unittest.mock.patch(target, return_value=None):
        vm.validate()

    assert vm.error is None


def test_register_validation_for_existing_user():
    form_data = {
        'name': 'Kat',
        'email': 'katrinakay.alaimo@gmail.com',
        'password': 'kat'*3
    }

    with flask_app.test_request_context(path='/account/register', data=form_data):
        vm = RegisterViewModel()

    # Avoids database call on register
    target = 'pypi_org.services.user_service.find_user_by_email'
    test_user = User(email=form_data.get('email'))
    with unittest.mock.patch(target, return_value=test_user):
        vm.validate()

    assert vm.error is not None
    assert 'already exists' in vm.error


def test_register_validation_no_email():
    form_data = {
        'name': 'Kat',
        'email': '',
        'password': 'kat'*3
    }

    with flask_app.test_request_context(path='/account/register', data=form_data):
        vm = RegisterViewModel()

    vm.validate()

    assert vm.error is not None
    assert 'email' in vm.error


def test_register_validation_view_new_user():
    form_data = {
        'name': 'Kat',
        'email': 'katrinakay.alaimo@gmail.com',
        'password': 'kat'*3
    }

    target_find_user = 'pypi_org.services.user_service.find_user_by_email'
    target_create_user = 'pypi_org.services.user_service.create_user'
    find_user = unittest.mock.patch(target_find_user, return_value=None)
    create_user = unittest.mock.patch(target_create_user, return_value=User())
    request = flask_app.test_request_context(path='/account/register', data=form_data)
    with find_user, create_user, request:
        resp: Response = register_post()

    assert resp.location == '/account'


def test_account_home_no_login(client):
    target = 'pypi_org.services.user_service.find_user_by_id'
    with unittest.mock.patch(target, return_value=None):
        resp: Response = client.get('/account')

    assert resp.status_code == 302
    assert resp.location == 'http://localhost/account/login'


def test_account_home_with_login(client):
    target = 'pypi_org.services.user_service.find_user_by_id'
    test_user = User(name='Kat', email='katrinakay.alaimo@gmail.com')
    with unittest.mock.patch(target, return_value=test_user):
        resp: Response = client.get('/account')

    assert resp.status_code == 200
    assert b'Kat' in resp.data

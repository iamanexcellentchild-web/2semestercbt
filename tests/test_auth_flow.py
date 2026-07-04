import importlib

import app as app_module


def test_root_redirects_to_login_when_not_authenticated():
    app_module.app.config.update(TESTING=True)
    client = app_module.app.test_client()

    response = client.get('/')

    assert response.status_code == 302
    assert response.headers['Location'].endswith('/login')


def test_login_page_redirects_to_home_when_already_authenticated():
    app_module.app.config.update(TESTING=True)
    client = app_module.app.test_client()

    with client.session_transaction() as session:
        session['username'] = 'Ada'

    response = client.get('/login')

    assert response.status_code == 302
    assert response.headers['Location'].endswith('/')


def test_authenticated_user_can_reach_homepage():
    app_module.app.config.update(TESTING=True)
    client = app_module.app.test_client()

    with client.session_transaction() as session:
        session['username'] = 'Ada'

    response = client.get('/')

    assert response.status_code == 200
    assert b'Welcome back' in response.data

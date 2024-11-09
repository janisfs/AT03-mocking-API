import pytest
from github_api import get_github_user
from pytest_mock import mocker



def test_get_github_user_with_error(mocker):
    mock_get = mocker.patch('github_api.requests.get')
    mock_get.return_value.status_code = 404


    user_data = get_github_user('johndoe')
    assert user_data == None


def test_get_github_user(mocker):
    mock_get = mocker.patch('github_api.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'name': 'John Doe',
        'id': 12345,
        'company': 'Acme Inc.',
        'email': '4X3Zd@example.com'
    }


    user_data = get_github_user('johndoe')

    assert user_data == {
        'name': 'John Doe',
        'id': 12345,
        'company': 'Acme Inc.',
        'email': '4X3Zd@example.com'

    }

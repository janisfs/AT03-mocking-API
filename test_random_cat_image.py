import pytest
from random_cat_image import get_random_cat_image
from pytest_mock import mocker

def test_success(mocker):
    url = get_random_cat_image()
    assert url is not None
    assert isinstance(url, str)

def test_failure(mocker):
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 404
    url = get_random_cat_image()
    assert url is None
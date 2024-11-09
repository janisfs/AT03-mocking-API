import pytest
from main import get_weather
from pytest_mock import mocker

def test_get_weather(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'Sunny'}],
        'main': {'temp': 25}
    }

    api_key = 'd9a0f4c37c536dec3b20825900c97115'
    city = 'London'
    weather_data = get_weather(api_key, city)

    assert weather_data['weather'][0]['description'] == 'Sunny'
    assert weather_data['main']['temp'] == 25


def test_get_weather_with_error(mocker_):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404

    api_key = 'd9a0f4c37c536dec3b20825900c97115'
    city = 'London'
    weather_data = get_weather(api_key, city)
    assert weather_data is None


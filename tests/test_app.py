import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, template_rendered, request
from app import app, get_weather_data, index, history
import os
class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    @patch('app.requests.get')
    def test_get_weather_data_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "coord": {
                "lon": 31.2497,
                "lat": 30.0626
            },
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03d"
                }
            ],
            "base": "stations",
            "main": {
                "temp": 15.42,
                "feels_like": 14.09,
                "temp_min": 15.23,
                "temp_max": 15.42,
                "pressure": 1023,
                "humidity": 41,
                "sea_level": 1023,
                "grnd_level": 1017
            },
            "visibility": 10000,
            "wind": {
                "speed": 6.17,
                "deg": 40
            },
            "clouds": {
                "all": 40
            },
            "dt": 1740480693,
            "sys": {
                "type": 1,
                "id": 2514,
                "country": "EG",
                "sunrise": 1740457531,
                "sunset": 1740498658
            },
            "timezone": 7200,
            "id": 360630,
            "name": "Cairo",
            "cod": 200
        }
        mock_get.return_value = mock_response

        result = get_weather_data('Cairo')
        self.assertEqual(result['name'], 'Cairo')
        self.assertEqual(result['weather'][0]['main'], 'Clouds')

    @patch('app.requests.get')
    def test_get_weather_data_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = get_weather_data('ABCDD')
        self.assertIsNone(result)

    @patch('app.get_weather_data')
    @patch('app.save_weather_query')
    def test_index_post_success(self, mock_save_weather_query, mock_get_weather_data):
        mock_get_weather_data.return_value = {
            "coord": {
                "lon": 31.2497,
                "lat": 30.0626
            },
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03d"
                }
            ],
            "base": "stations",
            "main": {
                "temp": 15.42,
                "feels_like": 14.09,
                "temp_min": 15.23,
                "temp_max": 15.42,
                "pressure": 1023,
                "humidity": 41,
                "sea_level": 1023,
                "grnd_level": 1017
            },
            "visibility": 10000,
            "wind": {
                "speed": 6.17,
                "deg": 40
            },
            "clouds": {
                "all": 40
            },
            "dt": 1740480693,
            "sys": {
                "type": 1,
                "id": 2514,
                "country": "EG",
                "sunrise": 1740457531,
                "sunset": 1740498658
            },
            "timezone": 7200,
            "id": 360630,
            "name": "Cairo",
            "cod": 200
        }
        response = self.client.post('/', data={'city': 'Cairo'})
        self.assertEqual(response.status_code, 200)
        mock_save_weather_query.assert_called_once()

    @patch('app.get_weather_data')
    def test_index_post_failure(self, mock_get_weather_data):
        mock_get_weather_data.return_value = None
        response = self.client.post('/', data={'city': 'ABCDD'})
        self.assertEqual(response.status_code, 200)

    @patch('app.get_weather_history')
    def test_history(self, mock_get_weather_history):
        mock_get_weather_history.return_value = [{
            'query_timestamp': '2025-02-25 10:55:06.786235',
            'city': 'Cairo',
            'weather_main': 'Clear',
            'weather_description': 'clear sky',
            'temperature': 20,
            'temperature_feels_like': 18,
            'humidity': 75,
            'pressure': 1000,
            'wind_speed': 2.38,
            'wind_direction': 'South',
            'sunrise': '06:00',
            'sunset': '18:00',
            'data_calculation':'12:34'

        }]
        response = self.client.get('/history')
        self.assertEqual(response.status_code, 200)
if __name__ == '__main__':
    unittest.main()

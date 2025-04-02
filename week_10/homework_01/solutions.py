import unittest
import requests
from unittest.mock import patch


def calculate_average(numbers):
    if not numbers:
        raise ValueError("List is empty")
    return sum(numbers) / len(numbers)


class TestCalculateAverage(unittest.TestCase):
    def test_calculate_average_whole(self):
        self.assertEqual(calculate_average([2, 4, 6]), 4)

    def test_calculate_average_decimal(self):
        self.assertAlmostEqual(calculate_average([1, 2]), 1.5)

    def test_calculate_average_empty(self):
        with self.assertRaises(ValueError):
            calculate_average([])


def get_weather(city):
    try:
        response = requests.get(f"https://api.weather.com/v1/weather?q={city}")
        if response.status_code == 200:
            return response.json()
        return None
    except requests.exceptions.RequestException:
        return None


class TestGetWeather(unittest.TestCase):
    @patch('requests.get')
    def test_get_weather_request_made(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"weather": "sunny"}
        result = get_weather("Kyiv")
        mock_get.assert_called_with("https://api.weather.com/v1/weather?q=Kyiv")
        self.assertEqual(result, {"weather": "sunny"})


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
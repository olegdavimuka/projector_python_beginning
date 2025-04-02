import csv
import unittest
from unittest.mock import mock_open, patch

def read_temperatures_fahrenheit(input_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        return [float(row[0]) for row in reader]


def fahrenheit_to_celsius(f_temp):
    FAHRENHEIT_OFFSET = 32
    FAHRENHEIT_RATIO = 5 / 9
    return (f_temp - FAHRENHEIT_OFFSET) * FAHRENHEIT_RATIO


def convert_temperatures_to_celsius(fahrenheit_temps):
    return [fahrenheit_to_celsius(temp) for temp in fahrenheit_temps]


def calculate_statistics(celsius_temps):
    average = sum(celsius_temps) / len(celsius_temps)
    minimum = min(celsius_temps)
    maximum = max(celsius_temps)
    return average, minimum, maximum


def write_celsius_temperatures(output_file, celsius_temps):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Temperature (C)'])
        for temp in celsius_temps:
            writer.writerow([temp])


def process_temperature_data(input_file, output_file):
    fahrenheit_temps = read_temperatures_fahrenheit(input_file)
    celsius_temps = convert_temperatures_to_celsius(fahrenheit_temps)
    average, minimum, maximum = calculate_statistics(celsius_temps)

    print("Statistics:")
    print("Average: {:.2f}°C".format(average))
    print("Minimum: {:.2f}°C".format(minimum))
    print("Maximum: {:.2f}°C".format(maximum))

    write_celsius_temperatures(output_file, celsius_temps)

class UnitTestCase(unittest.TestCase):
    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0.0)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100.0)

    def test_convert_temperatures_to_celsius(self):
        result = convert_temperatures_to_celsius([32, 212])
        self.assertEqual([round(r, 2) for r in result], [0.0, 100.0])

    def test_calculate_statistics(self):
        temps = [0.0, 50.0, 100.0]
        avg, mi, ma = calculate_statistics(temps)
        self.assertAlmostEqual(avg, 50.0)
        self.assertEqual(mi, 0.0)
        self.assertEqual(ma, 100.0)

class IntegrationTestCase(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="Temperature (F)\n32\n212\n")
    def test_process_temperature_data(self, mock_file):
        with patch("csv.writer") as mock_writer:
            mock_writer_instance = mock_writer.return_value
            process_temperature_data("input.csv", "output.csv")
            mock_writer_instance.writerow.assert_any_call(['Temperature (C)'])
            mock_writer_instance.writerow.assert_any_call([0.0])
            mock_writer_instance.writerow.assert_any_call([100.0])

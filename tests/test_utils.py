from utils import timestamp_to_hms_format, wind_direction, hpa_to_mmhg
import unittest


class TestUtils(unittest.TestCase):
    def test_timestamp_to_hms_format(self):
        timestamp = 1740477181
        timezone_offset = 10800
        self.assertEqual(timestamp_to_hms_format(timestamp,timezone_offset),  "12:53:01")

    def test_wind_direction(self):
        self.assertEqual(wind_direction(0),"North")
        self.assertEqual(wind_direction(45),"Northeast")
        self.assertEqual(wind_direction(90),"East")
        self.assertEqual(wind_direction(135),"Southeast")
        self.assertEqual(wind_direction(180),"South")
        self.assertEqual(wind_direction(225),"Southwest")
        self.assertEqual(wind_direction(270),"West")
        self.assertEqual(wind_direction(315),"Northwest")

    def test_hpa_to_mmhg(self):
        pressure=1021
        self.assertEqual(hpa_to_mmhg(pressure),  765)

if __name__ == '__main__':
    unittest.main()


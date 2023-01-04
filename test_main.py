from unittest import TestCase
from main import calculate_remaining_power


class Test(TestCase):
    def test_calculate_remaining_power(self):
        self.assertEqual(calculate_remaining_power(200, 0, 0, 6, 6, "N"), 75)
        self.assertEqual(calculate_remaining_power(200, 2, 2, 2, 2, "S"), 200)
        self.assertEqual(calculate_remaining_power(200, 2, 1, 4, 1, "E"), 180)
        self.assertEqual(calculate_remaining_power(200, 2, 1, 4, 5, "S"), 130)
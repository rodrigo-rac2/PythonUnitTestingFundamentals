# Topics: two classes

import unittest
from unit_testing_02.calculator_v3 import Calculator


class TestsCalculatorAddFunctionality(unittest.TestCase):
    def add_two_positive_numbers(self):
        calc = Calculator(10, 20)
        result = calc.calc_add()
        self.assertEqual(result, 30)

    def add_one_positive_number_and_one_negative(self):
        calc = Calculator(50, -90)
        result = calc.calc_add()
        self.assertEqual(result, -40)

    def test_add_two_negative_numbers(self):
        calc = Calculator(-10, -20)
        result = calc.calc_add()
        self.assertEqual(result, -30)

    def test_add_two_positive_decimal_numbers(self):
        calc = Calculator(10.55, 20.97)
        result = calc.calc_add()
        self.assertEqual(result, 31.52)

    @unittest.skip("Waiting on BA...")
    def test_add_two_positive_decimal_numbers_with_ten_decimal_places(self):
        pass

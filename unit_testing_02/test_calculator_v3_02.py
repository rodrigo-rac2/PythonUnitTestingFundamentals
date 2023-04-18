# Topics: two classes

import unittest
from unit_testing_02.calculator_v3 import Calculator


class TestsCalculatorBaseFunctionality(unittest.TestCase):
    def test_add(self):
        calc = Calculator(10, 20)
        result = calc.calc_add()
        self.assertEqual(result, 30)

    def test_diff(self):
        calc = Calculator(100, 20)
        result = calc.calc_diff()
        self.assertEqual(result, 80)

    def test_prod(self):
        calc = Calculator(10, 20)
        result = calc.calc_prod()
        self.assertEqual(result, 200)


class TestsCalculatorAddFunctionality(unittest.TestCase):
    def test_add_two_positive_numbers(self):
        calc = Calculator(10, 20)
        result = calc.calc_add()
        self.assertEqual(result, 30)

    def test_add_one_positive_number_and_one_negative(self):
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

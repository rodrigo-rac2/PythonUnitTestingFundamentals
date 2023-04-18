# Topics: Know Exceptions

import unittest
from unit_testing_02.calculator_v3 import Calculator


class TestsCalculatorAddFunctionality(unittest.TestCase):
    def test_add_two_positive_numbers(self):
        calc = Calculator(10, 20)
        result = calc.calc_add()
        self.assertEqual(result, 30)

    def test_add_one_number_and_one_string_a(self):
        calc = Calculator(10, "Python")
        result = calc.calc_add()
        self.assertEqual(result, 30)

    def test_add_one_number_and_one_string_b(self):
        calc = Calculator(10, "Python")
        with self.assertRaises(TypeError):
            result = calc.calc_add()
            self.assertEqual(result, 30)
            print("Hello")

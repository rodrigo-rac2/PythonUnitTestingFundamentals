# Topics: One Class

import unittest
from unit_testing_02.calculator_v3 import Calculator


class TestsCalculatorBase(unittest.TestCase):
    """
    Tests for the base functionality of the calculator class
    """
    def test_add_using_two_positive_numbers(self):
        """
        Test case to test add functionality with two positive numbers
        """
        calc = Calculator(10, 20)
        result = calc.calc_add()
        self.assertEqual(result, 30)

    @unittest.skip("Just for fun...")
    def test_add_using_one_negative_number(self):
        """
        Test case to test add functionality with one positive number
        and one negative number
        """
        calc = Calculator(10, -20)
        result = calc.calc_add()
        self.assertEqual(result, -10)

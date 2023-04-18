"""
Topics:
    Test Suite >>>>>
        A test suite is a collection of test cases, test suites, or both.
        It is used to aggregate tests that should be executed together.
    Test runner >>>>>
        A test runner is a component which orchestrates the execution of tests and
        provides the outcome to the user. The runner may use a graphical interface,
        a textual interface, or return a special value to indicate the results of
        executing the tests.
"""

# 1. Import unittest & the required modules
import unittest
from unit_testing_02 import test_calculator_v3_01
from unit_testing_02 import test_calculator_v3_02
from unit_testing_02 import test_calculator_v3_03
from unit_testing_02 import test_calculator_v3_04

# 2. Create an instance of the TestLoader
loader = unittest.TestLoader()

# 3. Create an instance of TestSuite
suite = unittest.TestSuite()

# 4. Add Test Cases to the TestSuite instance
# >> Load test cases from a module
suite.addTests(loader.loadTestsFromModule(test_calculator_v3_01))
suite.addTests(loader.loadTestsFromModule(test_calculator_v3_02))

# >> Load test cases from a class
suite.addTests(loader.loadTestsFromTestCase(test_calculator_v3_03.TestsCalculatorAddFunctionality))

# 5. Create an instance of TextTestRunner
runner = unittest.TextTestRunner(verbosity=1)

# 6. Run the TextTestRunner instance
# test_results = runner.run(suite)

# total_ran = test_results.testsRun
# total_skipped = len(test_results.skipped)
# total_errors = len(test_results.errors)
# total_failed = len(test_results.failures)

# print("Total Ran        : " + str(total_ran))
# print("Total Skipped    : " + str(total_skipped))
# print("Total Errors     : " + str(total_errors))
# print("Total Failed     : " + str(total_failed))


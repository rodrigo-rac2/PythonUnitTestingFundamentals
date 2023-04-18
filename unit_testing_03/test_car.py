import unittest
from unit_testing_03.car import Car


class TestCarFunctionality(unittest.TestCase):
    def test_start_car(self):
        car1 = Car("VW", "Passat", "2017")
        car1.start()
        self.assertEqual(car1.isEngineStarted, True)
        car1.accelerate(10)
        self.assertEqual(car1.speed, 10)

    def test_car_breaks(self):
        car1 = Car("VW", "Passat", "2017")
        car1.start()
        self.assertEqual(car1.isEngineStarted, True)
        car1.accelerate(10)
        car1.accelerate(20)
        car1.accelerate(25)
        car1.apply_breaks(3)
        self.assertEqual(car1.speed, (55 - 3 * car1.decrease_in_speed_per_second_of_breaks))

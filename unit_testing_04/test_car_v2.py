import unittest
from unit_testing_04.car import Car


class TestCarFunctionality(unittest.TestCase):
    def test_start_the_car(self):
        car1 = Car("VW", "Passat", "2017")
        car1.start()
        self.assertEqual(car1.isEngineStarted, True)

    def test_check_acceleration(self):
        car1 = Car("VW", "Passat", "2017")
        car1.start()
        car1.accelerate(10)
        self.assertEqual(car1.speed, 10)

    def test_verify_default_seating_capacity(self):
        car1 = Car("VW", "Passat", "2017")
        # car1.seating_capacity = 6
        self.assertEqual(car1.seating_capacity, 5)

    def test_verify_non_default_seating_capacity(self):
        car1 = Car("VW", "Passat", "2017")
        car1.seating_capacity = 6
        self.assertEqual(car1.seating_capacity, 6)

    def test_stop_the_car(self):
        car1 = Car("VW", "Passat", "2017")
        car1.start()
        car1.stop()
        self.assertEqual(car1.isEngineStarted, False)

    def test_car_breaks(self):
        car1 = Car("VW", "Passat", "2017")
        car1.start()
        apply_break_for_in_seconds = 4
        car1.accelerate(10)
        car1.accelerate(20)
        car1.accelerate(25)
        car1.apply_breaks(apply_break_for_in_seconds)
        self.assertEqual(car1.speed, (55 - apply_break_for_in_seconds * car1.decrease_in_speed_per_second_of_breaks))

    def test_check_usb_port_base_car_trim(self):
        car1 = Car("VW", "Passat", "2017")
        self.assertEqual(car1.usb_port, False)

    def test_check_usb_port_premium_car_trim(self):
        car1 = Car("VW", "Passat", "2017")
        car1.usb_port = True
        self.assertEqual(car1.usb_port, True)


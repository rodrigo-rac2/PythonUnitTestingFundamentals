
class Car:
    """
    Car class
    """
    decrease_in_speed_per_second_of_breaks = 5

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
        self.isEngineStarted = False
        self.seating_capacity = 5
        self.cd_player = True
        self.bluetooth = False
        self.usb_port = False

    def start(self):
        """
        This method starts the car object.
        Sets the "isEngineStarted" property to True
        """
        self.isEngineStarted = True

    def stop(self):
        """
        This method stops the car object.
        Sets the "isEngineStarted" property to False
        """
        if self.isEngineStarted:
            self.isEngineStarted = False

    def current_speed(self):
        """
        Returns the current speed of the car object
        :returns: speed property
        """
        return self.speed

    def accelerate(self, increase_speed_by):
        """
        This method increases speed by the number passed!
        """
        if self.isEngineStarted:
            self.speed += increase_speed_by

    def decelerate(self, decrease_speed_by):
        """
        This method decreases speed by the number passed!
        """
        if self.isEngineStarted:
            self.speed -= decrease_speed_by
        if self.speed < 0:
            self.speed = 0

    def apply_breaks(self, apply_breaks_for_in_seconds):
        """
        This method decreases speed by 5 per every second!
        """
        self.speed = self.speed - apply_breaks_for_in_seconds * self.decrease_in_speed_per_second_of_breaks
        if self.speed < 0:
            self.speed = 0


if __name__ == '__main__':
    print("Import and use it!")

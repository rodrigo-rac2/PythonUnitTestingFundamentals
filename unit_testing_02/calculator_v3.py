
class Calculator:
    """
    Basic Calculator class.
    Constructor requires two numbers (num1 and num2)
    """
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calc_add(self):
        """
        Returns the sum of two numbers
        :return: num1 + num2
        """
        return self.num1 + self.num2

    def calc_diff(self):
        """
        Returns the difference between the numbers
        :returns: num1 - num2
        """
        return self.num1 - self.num2

    def calc_prod(self):
        """
        Returns the product of numbers
        :returns: num1 * num2
        """
        return self.num1 * self.num2


if __name__ == '__main__':
    print("Import and use it!")

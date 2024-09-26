class Calculator:
    def __init__(self, initial_value):
        self.value = (initial_value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("The value must be a number.")
        self._value = value

    def __str__(self):
        return f"The current value is {self.value}."

    def add(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError("The other value must be a number.")
        self.value += other
        return self.value

    def subtract(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError("The other value must be a number.")
        if self.value - other < 0:
            raise ValueError("The result would be negative.")
        self.value -= other
        return self.value

    def multiply(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError("The other value must be a number.")
        self.value *= other
        return self.value

    def divide(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError("The other value must be a number.")
        if other == 0:
            raise ValueError("Cannot divide by zero.")
        self.value /= other
        return self.value


if __name__ == "__main__":
    calc = Calculator(10)
    print(calc)



class Point():
    """ Representing an Point on the cartesian plane """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("x must be a number.")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("y must be a number.")
        self._y = value


if __name__ == "__main__":
    p = Point(10, 20)
    print(f"Point coordinates: ({p.x}, {p.y})")

    # p.x = "invalid"
    p.y = 30.5

    print(f"Point coordinates: ({p.x}, {p.y})")

    try:
        p.x = "invalid"
        p.y = "invalid"
    except ValueError as error:
        print(f"An ocurred error occurred: {error}")

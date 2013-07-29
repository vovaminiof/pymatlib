# intergals.py
from funcparser import Parser

class Integral(object):
    def __init__(self, function, a, b):
        parser = Parser(function)
        self.f = parser.func
        self.max_power = parser.power
        self.a = a
        self.b = b
        self._value = None
        self._calc()

    def _calc(self):
        self.n = 150000
        if self.max_power == 0:
            self._value = self.__rectangle_rule()
        if self.max_power == 1:
            self._value = self.__trapezoidal_rule()
        elif self.max_power >= 2:
            self._value = self.__simpsons_rule()

    def __rectangle_rule(self):
        h = float(self.b - self.a)/self.n
        result = 0.0
        for i in range(1, self.n + 1):
            result += self.f(self.a + (2*i - 1)*h/2.0)

        return h*result

    def __trapezoidal_rule(self):
        h = float(self.b - self.a)/self.n
        result = self.f(self.a) + self.f(self.b)
        for i in range(2, self.n):
            result += 2 * self.f(self.a + (i-1)*h)

        return h*result / 2.0

    def __simpsons_rule(self):
        h = float(self.b - self.a)/self.n
        result = self.f(self.a) + self.f(self.b)
        for i in range(1, self.n):
            index = 4 if i % 2 != 0 else 2
            result += index * self.f(self.a + i*h)

        return h*result / 3.0

    @property
    def value(self):
        return self._value
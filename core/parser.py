# parser.py
import imp
import math

class Parser(object):

    def __init__(self, function):
        self._function = self.__parse_str(function)

    def __parse_str(self, f):
        ''' Parsing string function into lambda '''

        code = "def f(x): return " + f
        module = imp.new_module('calculus')
        exec code in math.__dict__, module.__dict__
        return module.f

    @property
    def func(self):
        return self._function
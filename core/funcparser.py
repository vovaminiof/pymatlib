# funcparser.py
import re
import imp
import math

class Parser(object):

    def __init__(self, function):
        def translate(f):
            return re.sub('(x[^^])', 'x^1', f)

        def power(f):
            return re.sub('x\^(\d+)', lambda g: 'pow(x,%s)' % g.group(1), f)

        f = function + ' '
        f = translate(f)
        self._max_power = self.__get_max_power(f)
        f = power(f)
        self._function = self.__parse_str(f)

    def __get_max_power(self, f):
        powers = re.findall('\^(\d)', f)
        return int(max(powers if powers else [0]))

    def __parse_str(self, f):
        ''' Parsing string function into lambda '''
        code = "def f(x): return " + f
        module = imp.new_module('calculus')
        exec code in math.__dict__, module.__dict__
        return module.f

    @property
    def func(self):
        return self._function

    @property
    def power(self):
        return self._max_power
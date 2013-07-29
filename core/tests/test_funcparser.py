# test_funcparser.py
import os 
import sys

path = os.getcwd().rsplit('\\', 1)[0]
sys.path.append(path)

import unittest
from funcparser import Parser

class TestParser(unittest.TestCase):
	
	def test_parser(self):
		self.assertEqual(Parser('x^2 + x + 2').power, 2)
		self.assertEqual(Parser('x + 2').power, 1)
		self.assertEqual(Parser('2').power, 0)
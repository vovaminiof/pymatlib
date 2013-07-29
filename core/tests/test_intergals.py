# test_intergals.py

import os
import sys

sys.path.append(os.getcwd().rsplit('\\', 1)[0])

import unittest
from intergals import Integral

class TestIntegral(unittest.TestCase):

	def test_0_power_function(self):
		self.assertAlmostEqual(Integral('2', 0, 1).value, 2)
		self.assertAlmostEqual(Integral('2', 1, 10).value, 18)
		self.assertAlmostEqual(Integral('2', 10, 1).value, -18)

	def test_1_power_function(self):
		self.assertAlmostEqual(Integral('2*x + 2', 0, 1).value, 3, delta=0.01)
		self.assertAlmostEqual(Integral('2*x + 2', 1, 10).value, 117, delta=0.01)
		self.assertAlmostEqual(Integral('2*x + 2', 10, 1).value, -117, delta=0.01)

	def test_2_power_function(self):
		self.assertAlmostEqual(Integral('6*x^2 + 2*x + 2', 0, 1).value, 5)
		self.assertAlmostEqual(Integral('6*x^2 + 2*x + 2', 1, 10).value, 2115)
		self.assertAlmostEqual(Integral('6*x^2 + 2*x + 2', 10, 1).value, -2115)
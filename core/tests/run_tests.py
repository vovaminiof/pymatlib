# run_tests.py
import unittest2 as unittest

if __name__ == '__main__':
	all_tests = unittest.TestLoader().discover('', pattern='test_*.py')
	unittest.TextTestRunner().run(all_tests)
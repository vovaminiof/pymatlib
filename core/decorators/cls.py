# decorators.py
import time
def timer(cls):
	cls_init = cls.__init__

	def init(self, function, a, b):
		start = time.time()
		cls_init(self, function, a, b)
		print time.time() - start

	cls.__init__ = init
	return cls
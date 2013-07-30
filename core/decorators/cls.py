# decorators.py
import time

def timer(cls):
    cls_init = cls.__init__

    def init(self, *args, **kwargs):
        start = time.time()
        cls_init(self, *args, **kwargs)
        print time.time() - start

    cls.__init__ = init
    return cls
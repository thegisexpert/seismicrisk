import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        print (self.assertEqual(fun(3), 5))
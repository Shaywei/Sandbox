import unittest
import foo

class TestFoo(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(2, foo.foo())
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_bar_to_tick']
    unittest.main()        
import unittest

from ..aSingleton import *

class TestSingleton(unittest.TestCase):

    def setUp(self):
        self.a = TestSingletone()
        self.b = TestSingletone()

    def test_singleInstance(self):
        self.assertEqual( self.a.get_name() , self.b.get_name())
        self.assertEqual( id(self.a),id(self.b))
        self.assertEqual( self.a , self.b)
        self.a.set_name('Test')
        self.assertEqual( self.a , self.b)
        self.b.set_name('Test2')
        self.assertEqual( self.a , self.b)
        self.b.set_name('Test3')
        self.assertEqual( self.a.get_name() , self.b.get_name())
        self.assertEqual( self.a.get_name() , 'Test3')
        self.assertEqual( self.b.get_name() , 'Test3')


if __name__ == '__main__':
    unittest.main()

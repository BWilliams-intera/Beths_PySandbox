#My first test unit

import unittest 
from Hello_World import *

class HelloWorldTest(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_c1(self):
        c1 = MyClass(2, 3)
        z = c1.add_nums()
        self.assertEqual( z, 5)
    
    def test_c2(self):
        c2 = MyClass(5,10)
        z = c2.add_nums()
        self.assertEqual( z, 15)
        
class HelloWorldTest2(unittest.TestCase):
    
    def test_c3(self):
        c3 = NewClass1(2,3)
        z = c3.add_nums()
        q = c3.sub_nums()
        self.assertEqual(z, 8)
        self.assertEqual(q, -1)
        

    
if __name__ == '__main__':
    unittest.main()
    

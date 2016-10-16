import unittest
from underscore import Underscore

class UnderscoreTest(unittest.TestCase):
    def setUp(self):
        # create an instance of the Underscore module we created
        self._ = Underscore()
        # initialize a list to run our tests on
        self.test_list = [1,2,3,4,5]
    def testMap(self):
        test=self._.map(self.test_list, lambda x: x*2)
        return self.assertEqual([2,4,6,8,10],test)
    def testReduce(self):
        test=self._.reduce(self.test_list, lambda x,y: x+y, 0)
        return self.assertEqual(15, test)
    def testFind(self):
        test=self._.find(self.test_list, lambda x: x%2==0)
        return self.assertTrue(test)
    def testFilter(self):
        test=self._.filter(self.test_list, lambda x: x%2==0)
        return self.assertEqual([2,4],test)
    def testReject(self):
        test=self._.reject(self.test_list, lambda x: x%2==0)
        return self.assertEqual([1,3,5],test)

if __name__ == "__main__":
    unittest.main()

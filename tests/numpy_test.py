import numpy
import unittest

class TesNumpy(unittest.TestCase):

    def test_random_randn(self):
        self.assertEqual(tuple, type(numpy.random.rand(2,3).shape))
        self.assertEqual((2, 3), numpy.random.rand(2,3).shape)

        self.assertEqual(tuple, type(numpy.random.rand(2,3, 4).shape))
        self.assertEqual((2, 3, 4), numpy.random.rand(2,3, 4).shape)

if __name__ == '__main__':
    unittest.main()

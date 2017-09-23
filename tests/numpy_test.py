import numpy
import unittest

class TesNumpy(unittest.TestCase):

    def test_random_randn(self):
        self.assertEqual(tuple, type(numpy.random.rand(2,3).shape))
        self.assertEqual((2, 3), numpy.random.rand(2,3).shape)

        self.assertEqual(tuple, type(numpy.random.rand(2,3, 4).shape))
        self.assertEqual((2, 3, 4), numpy.random.rand(2,3, 4).shape)

    def test_zeros(self):
        self.assertEqual(numpy.ndarray, type(numpy.zeros(5)))
        self.assertEqual((5, ), numpy.zeros(5).shape)

    def test_argmax(self):
        arr = numpy.array([1, 3, 5, 0, 9, 2])

        self.assertEqual(numpy.ndarray, type(arr))
        self.assertEqual(4, numpy.argmax(arr))

        arr2 = numpy.array([[1,9,3,5], [2,8,4,6]])

        self.assertEqual([1, 0, 1, 1], numpy.argmax(arr2, axis=0).tolist())

if __name__ == '__main__':
    unittest.main()

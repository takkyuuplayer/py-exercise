import unittest

class TestBasicFunctions(unittest.TestCase):

    def test_math_operation(self):
        self.assertEquals(3, 1 + 2)
        self.assertEquals(27, 3 ** 3)
        self.assertEquals(1.4, 7/5)

    def test_type(self):
        self.assertEquals(int, type(10))
        self.assertEquals(str, type('0'))
        self.assertEquals(float, type(1.5))
        self.assertEquals(list, type([1, 2, 3]))

    def test_variable(self):
        x = 10

        self.assertEqual(10, x)

    def test_list(self):
        a = [1, 2, 3, 4, 5]

        self.assertEqual(3, a[2])
        self.assertEqual(5, len(a))
        self.assertEquals([1,2,3,4,5], a)
        self.assertEquals([2,3,4], a[1:4])
        self.assertEquals(5, a[-1])
        self.assertEquals([1,2,3], a[:3])
        self.assertEquals([1,2,3,4], a[:-1])

        self.assertEquals([1,2,1,2,1,2], [1, 2] * 3)

    def test_dictionary(self):
        dic = {
                'height': 180,
                }

        self.assertEqual(180, dic['height'])

    def test_boolean(self):
        self.assertTrue(True)
        self.assertTrue(not False)

    def test_for_loop(self):
        arr = []
        for i in [1, 2, 3]:
            arr.append(i * i)

        self.assertEqual([1, 4, 9], arr)

    def test_func(self):
        self.assertEqual(3, self.add(1, 2))

    def add(self, a, b):
        return a + b

if __name__ == '__main__':
    unittest.main()


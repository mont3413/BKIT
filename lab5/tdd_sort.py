import unittest

from sort import sort_without_lambda, sort_with_lambda


class Test(unittest.TestCase):
    def test_sort_without_lambda(self):
        data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
        res = sort_without_lambda(data)
        exp = [123, 100, -100, -30, 4, -4, 1, -1, 0]
        self.assertEqual(res, exp)

    def test_sort_with_lambda(self):
        data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
        res = sort_with_lambda(data)
        exp = [123, 100, -100, -30, 4, -4, 1, -1, 0]
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()

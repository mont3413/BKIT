import unittest

from field import field


class Test(unittest.TestCase):
    def test_field_one_argument(self):
        goods = [
           {'title': 'Ковер', 'price': 2000, 'color': 'green'},
           {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
        ]
        res = field(goods, 'title')
        exp = ['Ковер', 'Диван для отдыха']
        self.assertEqual(res, exp)

    def test_field_many_arguments(self):
        goods = [
           {'title': 'Ковер', 'price': 2000, 'color': 'green'},
           {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
        ]
        res = field(goods, 'title', 'price')
        exp = [{'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}]
        self.assertEqual(res, exp)

if __name__ == "__main__":
    unittest.main()

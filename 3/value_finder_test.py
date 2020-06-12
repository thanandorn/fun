import unittest

from value_finder import get_value

class TestValueFinder(unittest.TestCase):
    def test_value_finder_first(self):
        obj = {"a":{"b":{"c":"d"}}}
        query_string = 'a/b/c'
        result = get_value(obj, query_string)
        self.assertEqual(result, 'd', 'The result should be d')
    def test_value_finder_second(self):
        obj = {"x":{"y":{"z":"a"}}}
        query_string = 'x/y/z'
        result = get_value(obj, query_string)
        self.assertEqual(result, 'a', 'The result should be a')

if __name__ == '__main__':
    unittest.main()

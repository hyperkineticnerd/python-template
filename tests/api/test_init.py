
import unittest

class TestSum(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_sum(self):
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result, 6, "Should be 6")

    def test_sum_tuple(self):
        data = (1,2,3)
        result = sum(data)
        self.assertEqual(result, 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()

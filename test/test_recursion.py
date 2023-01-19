import unittest
from modules.recursion import ReverseStringUsingRecursion


class TestRecursion(unittest.TestCase):
    def test_reverse_string_using_recursion(self):
        string = "hello world"
        self.assertEqual(ReverseStringUsingRecursion(
            string).reverse_string(), "dlrow olleh")


if __name__ == "__main__":
    unittest.main()

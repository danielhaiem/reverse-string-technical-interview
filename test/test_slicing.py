import unittest
from modules.slicing import ReverseStringUsingSlicing


class TestSlicing(unittest.TestCase):
    def test_reverse_string_using_slicing(self):
        string = "hello world"
        self.assertEqual(ReverseStringUsingSlicing(
            string).reverse_string(), "dlrow olleh")


if __name__ == "__main__":
    unittest.main()

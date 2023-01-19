import unittest
from modules.for_loop import ReverseStringUsingForLoop


class TestForLoop(unittest.TestCase):
    def test_reverse_string_using_for_loop(self):
        string = "hello world"
        self.assertEqual(
            ReverseStringUsingForLoop(string).reverse_string(), "dlrow olleh")


if __name__ == "__main__":
    unittest.main()

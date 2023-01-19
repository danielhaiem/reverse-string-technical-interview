import unittest
from modules.while_loop import ReverseStringUsingWhileLoop


class TestWhileLoop(unittest.TestCase):
    def test_reverse_string_using_while_loop(self):
        string = "hello world"
        self.assertEqual(ReverseStringUsingWhileLoop(
            string).reverse_string(), "dlrow olleh")


if __name__ == "__main__":
    unittest.main()

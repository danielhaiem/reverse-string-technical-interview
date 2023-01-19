import unittest
from modules.join_reversed import ReverseStringUsingJoinReversed


class TestJoinReversed(unittest.TestCase):
    def test_reverse_string_using_join_reversed(self):
        string = "hello world"
        self.assertEqual(
            ReverseStringUsingJoinReversed(string).reverse_string(), "dlrow olleh")


if __name__ == "__main__":
    unittest.main()

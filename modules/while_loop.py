class ReverseStringUsingWhileLoop:
    """The while loop is used to iterate over a block of code as long as the test expression (condition) is true and joins each character in the beginning in order to reverse the string."""

    def __init__(self, string):
        self.string = string

    def reverse_string(self):
        reversed_string = ''
        index = len(self.string)
        while index > 0:
            reversed_string += self.string[index - 1]
            index = index - 1
        return reversed_string

    def __str__(self):
        return f'result of while_loop.py: {self.reverse_string()}'

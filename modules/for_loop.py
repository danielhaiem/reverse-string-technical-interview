class ReverseStringUsingForLoop:
    """The for loop iterates over the string in reverse order and adds each character to the reversed_string variable."""

    def __init__(self, string):
        self.string = string

    def reverse_string(self):
        reversed_string = ""
        for i in range(len(self.string) - 1, -1, -1):
            reversed_string += self.string[i]
        return reversed_string

    def __str__(self):
        return f'result of for_loop.py: {self.reverse_string()}'

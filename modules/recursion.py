class ReverseStringUsingRecursion:
    """The string is passed as an argument to the function and the first character is removed and the function is called again until the string is empty. The base case is when the string is empty, and the function returns the empty string. The recursive case is when the string is not empty, and the function returns the function call with the first character removed and the first character added to the end of the string."""

    def __init__(self, string):
        self.string = string

    def reverse_string(self):
        if len(self.string) == 0:
            return self.string
        else:
            return ReverseStringUsingRecursion(self.string[1:]).reverse_string() + self.string[0]

    def __str__(self):
        return f'result of recursion.py: {self.reverse_string()}'

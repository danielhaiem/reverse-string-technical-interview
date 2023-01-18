class ReverseStringUsingJoinReversed:
    """
    The reversed function returns an iterator that accesses the given sequence in the reverse order. The join function joins all the elements of an iterable to make a string.
    """

    def __init__(self, string: str):
        self.string = string

    def reverse_string(self) -> str:
        return ''.join(reversed(self.string))

    def __str__(self):
        return f'result of join_reversed.py: {self.reverse_string()}'

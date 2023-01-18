class ReverseStringUsingSlicing:
    """
    The slice operator [start:stop:step] returns a slice of the list from the start index to the stop index. "-1" denotes the step size, which is negative, so the slice is done in reverse order.
    """

    def __init__(self, string: str):
        self.string = string

    def reverse_string(self) -> str:
        return self.string[::-1]

    def __str__(self):
        return f'result of slicing.py: {self.reverse_string()}'

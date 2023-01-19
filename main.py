import timeit
from modules.slicing import ReverseStringUsingSlicing
from modules.join_reversed import ReverseStringUsingJoinReversed
from modules.for_loop import ReverseStringUsingForLoop
from modules.recursion import ReverseStringUsingRecursion
from modules.while_loop import ReverseStringUsingWhileLoop


user_string = input("Enter a string: ")

reverse_string_methods = [
    ReverseStringUsingSlicing, ReverseStringUsingJoinReversed, ReverseStringUsingForLoop, ReverseStringUsingRecursion, ReverseStringUsingWhileLoop]

for method in reverse_string_methods:
    instance = method(user_string)
    start = timeit.default_timer()
    instance
    stop = timeit.default_timer()
    print(method.__str__(instance))
    print('Performance Evaluation Time: ', stop - start)

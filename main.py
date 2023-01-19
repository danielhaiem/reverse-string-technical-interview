import timeit
from modules.slicing import ReverseStringUsingSlicing
from modules.join_reversed import ReverseStringUsingJoinReversed


user_string = input("Enter a string: ")

reverse_string_methods = [
    ReverseStringUsingSlicing, ReverseStringUsingJoinReversed]

for method in reverse_string_methods:
    instance = method(user_string)
    start = timeit.default_timer()
    instance
    stop = timeit.default_timer()
    print(method.__str__(instance))
    print('Performance Evaluation Time: ', stop - start)

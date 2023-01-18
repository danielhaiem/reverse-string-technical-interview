import timeit
from modules.slicing import ReverseStringUsingSlicing

user_string = input("Enter a string: ")

reverse_string_methods = [ReverseStringUsingSlicing]

for method in reverse_string_methods:
    instance = method(user_string)
    start = timeit.default_timer()
    instance
    stop = timeit.default_timer()
    print(method.__str__(instance))
    print('Performance Evaluation Time: ', stop - start)

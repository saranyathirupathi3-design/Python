import itertools
counter = itertools.count(start=10)
first_five_numbers = itertools.islice(counter, 5)
result_list = list(first_five_numbers)
print(f"The first 5 numbers starting from 10 are: {result_list}")

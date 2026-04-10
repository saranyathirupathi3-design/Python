import itertools

def cycle_list_n_times(data_list, iterations):
    total_items = len(data_list) * iterations
    cycle_iterator = itertools.cycle(data_list)
    limited_cycle = itertools.islice(cycle_iterator, total_items)
    for item in limited_cycle:
        print(item)


my_list = [5, 10, 15]
num_iterations = 3
cycle_list_n_times(my_list, num_iterations)

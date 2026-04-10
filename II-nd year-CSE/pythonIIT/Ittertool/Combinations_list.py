import itertools
items = ['A', 'B', 'C', 'D']
combinations = itertools.combinations(items, 2)
combinations_list = list(combinations)
print(f"Original list: {items}")
print(f"Combinations of 2 items: {combinations_list}")
print("\nIterating through the combinations:")
for combo in itertools.combinations(items, 2):
    print(combo)

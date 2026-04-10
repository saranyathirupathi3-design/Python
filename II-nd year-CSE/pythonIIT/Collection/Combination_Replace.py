import itertools
data = [1, 2]
combinations = itertools.combinations_with_replacement(data, 2)
for combo in combinations:
    print(combo)


from collections import defaultdict

data = [("Alice",85),("Bob",78),("Alice",92),("Bob",88)]

d = defaultdict(list)

for name, mark in data:
    d[name].append(mark)

print(d)

from collections import ChainMap

d1 = {"a":10,"b":20}
d2 = {"b":30,"c":40}

c = ChainMap(d1, d2)

print(c["b"])   # takes from d1 first

from collections import OrderedDict

s = "swiss"
d = OrderedDict()

for ch in s:
    d[ch] = d.get(ch, 0) + 1

for k in d:
    if d[k] == 1:
        print(k)
        break

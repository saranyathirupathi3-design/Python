from itertools import *
import time
cc = cycle([ iter([1,2,3]), iter([4]) , iter([5,6]) ] )
p = 3
while p:
    try:
        for k in cc:
            print k.next()
    except StopIteration:
        p = p - 1
        cc = cycle(islice(cc,  p))  # this does not matter


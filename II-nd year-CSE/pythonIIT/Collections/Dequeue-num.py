from collections import deque

nums = [1,2,3,4,5,6]
k = 3

d = deque()
s = 0

for i in range(len(nums)):
    d.append(nums[i])
    s += nums[i]

    if len(d) > k:
        s -= d.popleft()

    if len(d) == k:
        print(s, end=" ")

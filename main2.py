import math

s = int(input())
t = int(input())
li = []
for i in range(t):
    li.append(int(input()))

if s == 0:
    print(max(li))
else:
    print(math.ceil((s + sum(li)) / t))
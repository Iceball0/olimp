k = int(input())
a, x = map(int, input().split())
b, y = map(int, input().split())
if x == 0 and a == 0 and (k - b) >= 0:
    print((k - b) * y)
elif a == 0 and b == 0:
    print(k * max(x, y))
elif a == b and (k - a) >= 0:
    print((k - a) * max(x, y))

else:
    print(0)

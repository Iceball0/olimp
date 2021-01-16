k = int(input())
a, x = map(int, input().split())
b, y = map(int, input().split())
if (k - a) * x >= (k - b) * y:
    if (k - a - b) >= 0:
        print((k - a) * x + (k - a - b) * y)
    elif (k - a) >= 0:
        print((k - a) * x)
elif (k - a) * x < (k - b) * y:
    if (k - a - b) >= 0:
        print((k - a - b) * x + (k - b) * y)
    elif (k - b) >= 0:
        print((k - b) * y)
else:
    print(0)

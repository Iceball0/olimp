res = 0
k = int(input())
a, x = map(int, input().split())
b, y = map(int, input().split())

if x

elif a != b:
    if b > a:
        k -= a
        res += x * k
        k -= b
        res += y * k
    elif a > b:
        k -= b
        res += y * k
        k -= a
        res += x * k
else:
    k -= a
    res += x * k + y * k
print(res)
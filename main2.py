t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    num12 = num34 = 10000
    m0 = n0 = 0
    for o in range(m, 0, -1):
        num1 = num2 = 0
        for r in range(n):
            for c in range(o):
                num1 += r * m + c + 1
            for c in range(o, m):
                num2 += r * m + c + 1
        if abs(num2 - num1) < num12:
            num12 = abs(num2 - num1)
        else:
            m0 = o + 1
            break
    for o in range(n, 0, -1):
        num3 = num4 = 0
        for r in range(o):
            for c in range(m):
                num3 += r * m + c + 1
        for r in range(o, n):
            for c in range(m):
                num4 += r * m + c + 1
        if abs(num4 - num3) < num34:
            num34 = abs(num4 - num3)
        else:
            n0 = o + 1
            break
    if num12 <= num34:
        print(f"V {m0 + 1}")
    else:
        print(f"H {n0 + 1}")

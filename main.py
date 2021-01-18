lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']

d, m, w = map(int, input().split())
i, j, k = map(int, input().split())

days_in_a_year = m * d
total_days = days_in_a_year * (k - 1) + d * (j - 1) + (i - 1)
print(lst[total_days % w])

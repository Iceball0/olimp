li = [3, 4, 5, 6]
print(li[(0 - 2) % len(li):] + li[:(0 - 2) % len(li)])
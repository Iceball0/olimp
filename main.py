import math

sev = math.ceil(int(input()) / 4)
ei = math.ceil(int(input()) / 4)
nin = math.ceil(int(input()) / 4)
res1 = ((sev + ei + nin) * 4)
res2 = math.ceil(sev / 3) + math.ceil(ei / 2) + nin
print(res1, res2)
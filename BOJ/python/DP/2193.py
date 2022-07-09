N = int(input())
pn = [0, 1, 1]
for i in range(3, 91):
  pn.append(pn[i - 2] + pn[i - 1])
print(pn[N])

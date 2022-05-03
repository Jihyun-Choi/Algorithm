N = int(input())
M = list(map(int, input().split()))
M.sort()
t=1
for i in M:
    if t<i:
        break
    t += i
print(t)

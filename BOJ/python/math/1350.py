N = int(input())
file = map(int, input().split())
cluster = int(input())
cnt = N
for f in file:
    if f > cluster:
        cnt += (f-1)//cluster
    elif f == 0:
        cnt -= 1
print(cluster*cnt)

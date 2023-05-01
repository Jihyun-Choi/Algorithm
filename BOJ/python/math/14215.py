rod = sorted(map(int, input().split()))
if rod[0] + rod[1] <= rod[2]:
    rod[2] = rod[0] + rod[1] - 1
print(sum(rod))

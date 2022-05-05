K = int(input())

money = []
for _ in range(K):
    m = int(input())
    if m == 0:
        money.pop()
    else:
        money.append(m)

print(sum(money))

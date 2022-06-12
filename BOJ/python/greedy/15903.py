N, M = map(int, input().split())
card = list(map(int, input().split()))
card.sort()
for _ in range(M):
    card.sort()
    card[0] = card[1] = card[0] + card[1] 
print(sum(card))

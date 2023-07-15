answer = []
for _ in range(2):
    T, F, S, P, C = list(map(int, input().split()))
    answer.append(T*6 + F*3 + S*2 + P + C*2)
print(*answer, sep=' ')

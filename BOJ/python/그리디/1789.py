# 1
s = int(input())
total = count = 0

while True:
    count += 1
    total += count
    if total > s:
        break
print(count-1)


# 2
S = int(input())
N = 1
while N * (N + 1) / 2 <= S:
    N += 1
print(N-1)


# 3
S = int(input())
print(int(((1 + S * 8)**.5 - 1)/2))

""" 1789
서로 다른 N개의 자연수의 합이 S일때, N이 최댓값이 될려면 1+2+3+...+..=S인 N의 개수를 구하면 된다.
# 1과 같이 반복문을 사용하여 N의 개수를 구해도 되지만 시간복잡도가 좋지 않으므로 다른 방법을 생각하는 것이 좋다.
"""

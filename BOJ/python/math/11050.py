from math import factorial
N, K = map(int, input().split())
B = factorial(N) // (factorial(K) * factorial(N - K))
print(B)

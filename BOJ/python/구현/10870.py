# 1
N = int(input())
fibo = [0, 1]

if N>1:
    for i in range(2, N+1):
        fibo.append(fibo[i-1] + fibo[i-2])
print(fibo[N])

# 2
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))

""" 10870
# 1 DP       30840 KB   68 ms
# 2 재귀함수  30840 KB  76 ms
"""

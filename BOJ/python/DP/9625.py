# 1
N = int(input())
A = [1]
B = [0]

for i in range(N):
    A.append(B[i])
    B.append(B[i] + A[i])
print(A[-1], B[-1])

# 2
N = int(input())
fibo = [0] * (N+1)
fibo[1] = 1
for i in range(2, N + 1):
    fibo[i] = fibo[i-1] +  fibo[i-2] 
print(fibo[N-1], fibo[N])

""" 9625
A                     1 0 
B                     0 1
BA                    1 1 
BAB                   1 2 
BA B BA               2 3
BAB BA BAB            3 5
BABBA BAB BABBA       
규칙을 찾기위해 위와 하나씩 적으면서 살펴봤는데, 문제의 조건만 잘 살펴봐도 바로 규칙을 알 수 있는 문제였다.
"""

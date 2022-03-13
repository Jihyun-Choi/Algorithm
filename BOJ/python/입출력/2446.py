N = int(input())

for i in range(1,N+1):
    print(" " * (i-1) + "*" * (((N-i)*2)+1))
for i in range(1,N):
    print(" " * (N-i-1) + "*" * ((2*i)+1))

"""
출력문에서 곱셈을 활용해 반복 출력할 때 연산은 괄호 안에 넣어주어야만 한다.
print("*" * i+1) 와 같이 코딩 시 TypeError가 발생한다.
왜냐하면 파이썬은 print(("*" * i)+1)로 인식하기 때문이다.
"""
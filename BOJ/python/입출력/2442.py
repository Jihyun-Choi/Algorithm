# 1
N = int(input())

for i in range(0,N):
    for j in range(0,N-1-i):
        print(" ", end="")
    for k in range(0,(i*2)+1):
        print("*", end="")
    print("")

# 2
N = int(input())
for i in range(1,N+1):
    print(' ' * (N-i) + '*' * (i*2-1))

"""
주로 cpp를 사용해 문제를 풀었던 기억때문인지, cpp와 비슷하게 python을 사용해 solve 한 것 같다.
python은 cpp와 다르게 곱셈연산을 활용하여 반복출력을 할 수 있다.
이러한 특징을 잘 활용하지 못하고 solve 중 이었던 것 같다...
#1과 #2는 메모리 크기는 동일하지만, #2가 #1보다 4ms가 더 빠르다. 차이는 미세한 것 같다.
"""
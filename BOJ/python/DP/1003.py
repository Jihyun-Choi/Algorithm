zero = [1, 0, 1]
one = [0, 1, 1]

def fibonacci(num):
    length = len(zero)  # 배열의 길이를 구해
    if num >= length:  # 입력받은 숫자가 배열의 길이보다 클 경우
        for i in range(length, num+1):  # 호출 횟수를 구함
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(zero[num], one[num])

T = int(input())
    
for _ in range(T):
    fibonacci(int(input()))


""" 1003
피보나치 값을 구하는 것이 아닌, 특정 피보나치를 구하기 위해 호출되는 호출횟수를 구하는 문제이다.
f(n) = f(n-1) + f(n-2)이므로,
f(n)의 f(0), f(1) 호출 횟수 = f(n-1)의 f(0), f(1) 호출 횟수 + f(n-2)의 f(0), f(1) 호출 횟수 이다.
"""

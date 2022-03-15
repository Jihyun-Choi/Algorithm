# 1 - 실패
def cycle(n):  # 한 자리수 n 일 경우 오류
    n = int(n)
    if n<10:
        n = n*10
    num = str(n)
    n = ((int(num[0]) + int(num[1])) % 10) + (int(num[1]) * 10)
    return int(n)


N = int(input())
sum = 0
num = N

while True:
    val = cycle(num)  # val을 num으로 쓰면 num = val 코드 삭제 가능
    if N == val:
        break
    sum += 1  # if문 위에 있어야 정상적으로 작동
    num = val

print(sum)


# 2 - # 1 수정 > 성공
def cycle(n):
    num = str(n)
    if n<10:
      num = "0" + num
    n = ((int(num[0]) + int(num[1])) % 10) + (int(num[1]) * 10)
    return int(n)

N = int(input())
sum = 0
num = N

while True:
    num = cycle(num)
    sum += 1
    if num == N:
        break

print(sum)

# 3 - 성공
N = int(input())
sum = 0
num = N

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c
    
    sum += 1
    if num == N:
        break

print(sum)
    
    
""" 1110
'먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고' 라는 부분을 5는 05가 아닌, 50으로 이해하여 #1과 같은 오류코드를 작성하였다. 
"""
A = int(input())
B = int(input())
C = int(input())

num = list(str(A*B*C))

for i in range(10):
    print(num.count(str(i)))  # count()함수 : 리스트에 찾고자 하는 원소의 개수를 반환

""" 입출력과 사칙연산
https://www.acmicpc.net/step/1
"""

# 2557
print("Hello World!")


# 10718
print("강한친구 대한육군")
print("강한친구 대한육군")


# 10171
print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \(__)|")

""" 10171
'\'를 출력할려면 '\\'와 같이 두 번 입력해줘야 '\'로 출력된다.
"""

# 10172
print("|\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print("||_/=\\\\__|")


# 1000
num=input().split()
print(int(num[0])+int(num[1]))


# 1001
num=input().split()
print(int(num[0])-int(num[1]))


# 10998
num=input().split()
print(int(num[0])*int(num[1]))


# 1008
num=input().split()
print(int(num[0])/int(num[1]))


# 10869
num=input().split()
print(int(num[0])+int(num[1]))
print(int(num[0])-int(num[1]))
print(int(num[0])*int(num[1]))
print(int(num[0])//int(num[1]))
print(int(num[0])%int(num[1]))


a,b = input().split()
print("%d\n%d\n%d\n%d\n%d"%(a+b, a-b, a*b, a/b, a%b))


# 10926
print(input() + "??!")


# 18108
print(int(input())-543)


# 10430
num = list(map(int, input().split()))

A = num[0]
B = num[1]
C = num[2]

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)


# 2588
X = int(input())
Y = input()

a = X * int(Y[2])
b = X * int(Y[1])
c = X * int(Y[0])
d = X * int(Y)

print(a, b, c, d, sep='\n') 

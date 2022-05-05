# 1
M = int(input())

sum = 1000 - M
n = 0

while (sum>0):
    if sum>500 and sum==500:
        n += 1
        sum -= 500
    elif sum>100 and sum==100:
        n += 1
        sum -= 100
    elif sum>50 and sum==50:
        n += 1
        sum -= 50
    elif sum>10 and sum==10:
        n += 1
        sum -= 10
    elif sum>5 and sum==5:
        n += 1
        sum -= 5
    elif sum>1 and sum==1:
        n += 1
        sum -= 1

print(n)


# 2
money = 1000 - int(input())
x = [500, 100, 50, 10, 5, 1]
c = 0

for i in x:
    c += money // i
    money %= i
print(c)

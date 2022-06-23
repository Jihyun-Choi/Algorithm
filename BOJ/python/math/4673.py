# 1
self_num = list(range(1, 10001))
x = []
for num in self_num :
    for n in str(num):
        num += int(n)
    if num <= 10000:
        x.append(num)
for remove_num in set(x):
    self_num.remove(remove_num)
for num in self_num:
    print(num)

# 2 - 출력 초과
self_num = list(range(1, 10001))
for num in self_num :
    for n in str(num):
        num += int(n)
    if num <= 10000 and (num in self_num):
        self_num.remove(num)
for num in self_num:
    print(num)

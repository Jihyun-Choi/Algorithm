n = []

for _ in range(0,9):
    n.append(int(input()))

n.sort(reverse=True)  # n리스트 내림차순 정렬

sum = sum(n)

x = y = 0

for i in range(0,8):
    for j in range(i+1,9): 
        if sum - (n[i] + n[j]) == 100:
            x = n[i]
            y = n[j]

n.remove(x) 
n.remove(y)         
n.sort()

for i in n:
    print(i)

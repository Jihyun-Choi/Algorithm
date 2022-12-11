T = int(input())
for _ in range(T):
    num = list(map(int, input().split()))
    even_num = [i for i in num if i % 2 == 0] 
    print(sum(even_num), min(even_num))

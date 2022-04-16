# 1
N = int(input())
house = []
for _ in range(N):
    house.append(list(map(int, input().split())))
for i in range(1,N):
    house[i][0] += min(house[i-1][1], house[i-1][2])
    house[i][1] += min(house[i-1][0], house[i-1][2])
    house[i][2] += min(house[i-1][0], house[i-1][1])
print(min(house[N-1]))


# 2
N = int(input())
house = []
for i in range(N):
    house.append(list(map(int, input().split())))
    if i != 0:
        house[i][0] += min(house[i-1][1], house[i-1][2])
        house[i][1] += min(house[i-1][0], house[i-1][2])
        house[i][2] += min(house[i-1][0], house[i-1][1])
print(min(house[N-1]))


# 3
N = int(input())
house = [0, 0, 0] 
for i in range(N):
    cost = [int(v) for v in input().split()]
    cost[0] += min(house[1], house[2])
    cost[1] += min(house[0], house[2])
    cost[2] += min(house[0], house[1])
    house = cost
print(min(house))


""" 1149
# 1 30840 KB	108 ms
# 2 30840 KB	116 ms
# 3 30840 KB	112 ms

시간복잡도를 줄이고자 # 1의 코드에서 # 2의 코드처럼 2개의 반복문을 하나로 합쳐보았다.
오히려 if문으로 인해 시간이 더 늘어났고, 곰곰히 생각해보니 반복문을 합친다고 반복횟수가 줄어드는 것은 아니므로 의미없는 짓이었다.

공간복잡도를 줄이고자 # 1의 코드에서 # 3의 코드처럼 리스트를 추가하지 않고 cost 리스트를 재활용해 값을 구해보았다.
메모리는 동일하였고, 오히려 시간이 늘어났다. 왜지...?
"""

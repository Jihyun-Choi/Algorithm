N = int(input())
test = list(map(int, input().split()))
max = max(test)
for i in range(N):
    test[i] = test[i]/max *100
print(sum(test)/N)

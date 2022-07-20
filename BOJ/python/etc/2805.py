N, M = map(int, input().split())
tree = list(map(int, input().split())) 
L, start, end = 0, 1, max(tree)
while start <= end:  
    mid = (start+end) // 2 
    for i in tree:
        if i >= mid:
            L += i - mid 
    if L >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)

N, M = map(int, input().split())
arr = list(map(int, input().split()))

def dfs(arr):
    result = {0:1}
    for i in arr:
        temp = result.copy()
        for j in temp:
            if j+i in temp:
                result[j+i] += temp[j]
            else:
                result[j+i] = temp[j]
    return result
        
if N == 1:
    print(1 if arr[0] == M else 0)
else:
    d1 = dfs(arr[:N//2])
    d2 = dfs(arr[N//2:])
    result = 0
    for a in d2:
        if M-a in d1:
            result += d1[M-a] * d2[a]
    if M == 0:
        result -= 1
    print(result)

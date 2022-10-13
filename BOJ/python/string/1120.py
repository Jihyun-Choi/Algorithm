str1, str2 = input().split()
diff = []
for i in range(len(str2) - len(str1) + 1): 
    cnt = 0
    for j in range(len(str1)):
        if str1[j] != str2[i + j]:
            cnt += 1
    diff.append(cnt)
print(min(diff))

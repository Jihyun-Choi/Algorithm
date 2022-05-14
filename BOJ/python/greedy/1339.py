N = int(input())
word = [list(map(lambda x: ord(x)-65, input().strip())) for _ in range(N)] 
A = [0] * 26 
for i in range(N):
    j = 0 
    for w in word[i][::-1]: 
        A[w] += (10 ** j) 
        j += 1 
A.sort(reverse=True) 
sum, v = 0, 9 
for i in range(26): 
    if A[i] == 0: 
        break 
    sum += (v * A[i]) 
    v -= 1
print(sum)

 
""" 1339
AABC와 같은 단어가 있을때, A는 1100, B는 10, C는 1로 치환 후 정렬하여 가장 큰 값부터 차례대로 9,8,7 ..을 곱한다.
ord() : 아스키코드 변환 함수
입력받은 알파벳을 아스키코드로 변환 후 'A'의 아스키코드 값을 뺄셈하여 알파벳을 0~25로 변환
"""

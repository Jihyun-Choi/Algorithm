N = int(input())
cnt = 0
for _ in range(N):
    word = input()
    for i in range(len(word)):
        if i != len(word)-1:
            if word[i] == word[i+1]:
                pass
            elif word[i] in word[i+1:]:
                break
        else:
            cnt += 1
print(cnt)

""" 1316
문자열을 반복문을 돌며 현재 문자가 다음 문자와 동일하다면 다음 코드로 넘어가고, 
현재 문자가 다음 문자와 동일하지 않다면, 현재 문자가 다음에 올 문자들과 동일한 문자가 있는지를 비교하여 검사한다.
"""

def solution(s):
    answer = ''
    flag = True
    for i in s:
        if flag: answer += i.upper()
        else: answer += i.lower() 
        flag = i.isspace() 
    return answer

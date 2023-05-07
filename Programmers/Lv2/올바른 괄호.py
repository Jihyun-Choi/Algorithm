def solution(s):
    answer = True 
    bracket = []
    for i in s:
        if i == '(': 
            bracket.append(1)
        else: 
            if not bracket: 
                return False
            bracket.pop()
    if not bracket: 
        return True
    else: 
        return False

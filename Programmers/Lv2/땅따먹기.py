def solution(land):
    for x in range(len(land)-1):
        row = land[x]
        for i in range(4): 
            land[x+1][i] += max(row[:i]+row[i+1:])
    answer = max(land[-1])
    return answer

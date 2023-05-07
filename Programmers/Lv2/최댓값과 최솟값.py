# 1
def solution(s):
    num = list(map(int, s.split()))
    answer = ' '.join([str(min(num))] + [str(max(num))])
    return answer

# 2
def solution(s):
    num = sorted(list(map(int, s.split())))
    answer = str(num[0]) + ' ' + str(num[-1])
    return answer

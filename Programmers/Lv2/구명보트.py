def solution(people, limit):
    answer = 0
    arr = sorted(people)
    i, j = 0, len(people)-1
    while i < j:
        if arr[i]+arr[j] <= limit:
            answer += 1
            i += 1
        j -= 1
    return len(people) - answer

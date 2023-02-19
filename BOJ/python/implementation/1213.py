from collections import Counter
name = input()
char_dict = Counter(name)
cnt = 0
answer, mid = '', ''
for k, v in sorted(char_dict.items()):
    if v % 2 == 1:
        cnt += 1
        mid = k 
        if cnt >= 2: 
            print("I'm Sorry Hansoo")
            exit()
    answer += (k * (v // 2))
print(answer + mid + answer[::-1])

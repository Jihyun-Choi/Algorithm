import sys
word = list(sys.stdin.readline())
i, start = 0, 0
while i < len(word):
    if word[i] == "<":
        i = word.index(">", i) + 1
    elif word[i].isalnum():
        start = i
        while i < len(word) and word[i].isalnum():
            i += 1
        tmp = word[start:i]
        tmp.reverse()
        word[start:i] = tmp
    else:
        i+=1
print("".join(word))

""" 17413
`print(*word, sep="")`보다 `print("".join(word))`가 16ms 더 빠름
"""

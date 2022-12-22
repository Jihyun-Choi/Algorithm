import sys
S, word = sys.stdin.read(), [0 for i in range(26)]
for c in S:
    if c.islower():
        word[ord(c)-97] += 1
for i in range(26):
    if word[i] == max(word):
        print(chr(i+97), end='')

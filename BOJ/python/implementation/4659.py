vowel = "aeiou"
while True:
    word = input()
    if word == "end" : break
    v, k = 0, 1
    for i in range(len(word)):
        if word[i] in vowel:
            v = 1
        if i > 0:
            if word[i] == word[i-1] and word[i] != 'e' and word[i] != 'o':
                k = 0
                break
        if i > 1:
            if word[i] not in vowel and word[i-1] not in vowel and word[i-2] not in vowel:
                k = 0
                break
            if word[i] in vowel and word[i-1] in vowel and word[i-2] in vowel:
                k = 0
                break
    if v == k == 1:
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")

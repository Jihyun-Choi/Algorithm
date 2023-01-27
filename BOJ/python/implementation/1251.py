word = input()
new_word = []
for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        word1 = word[0:i]
        word2 = word[i:j]
        word3 = word[j:]
        new_word.append(word1[::-1]+word2[::-1]+word3[::-1])
new_word.sort()
print(new_word[0])

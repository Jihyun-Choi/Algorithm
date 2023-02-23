word = input()
string = set()
for i in range(len(word)):
    for j in range(i, len(word)):
        string.add(word[i:j+1])
print(len(string))

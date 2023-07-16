word = input()
answer = []
for i in range(len(word)-1):
    for j in range(i+1, len(word)-1):
        X = word[:i+1][::-1] + word[i+1:j+1][::-1] + word[j+1:len(word)][::-1]
        answer.append(X)
print(min(answer))

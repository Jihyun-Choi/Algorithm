word1 = list(input())
word2 = list(input())
index = 0
while index < len(word1):
	if word1[index] in word2:
		word2.remove(word1[index])
		word1.remove(word1[index])
		index -= 1
	index += 1
print(len(word1) + len(word1))

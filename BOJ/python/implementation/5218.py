import sys
input = sys.stdin.readline
for _ in range(int(input())):
    distance = []
    word1, word2 = input().split()
    for i in range(len(word1)):
        if ord(word1[i]) > ord(word2[i]):
            distance.append(26 - (ord(word1[i])-ord(word2[i])))
        else:
            distance.append(ord(word2[i]) - ord(word1[i]))
    print("Distances:", *distance)

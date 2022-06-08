key = [[' '], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'],
            ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
p, w = map(int, input().split())
message = input()
t, k = 0, -1
for i in message:
    for j in range(len(key)):
        if (key[j].count(i)>0):
            t += (p*key[j].index(i)+p)
            if (k == j and i != ' ') : t+= w
            k = j
print(t)

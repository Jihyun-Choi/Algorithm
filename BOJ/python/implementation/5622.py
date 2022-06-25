dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
time = 0
for x in word:
    for i in dial:
        if x in i:
            time += dial.index(i)+3
print(time)

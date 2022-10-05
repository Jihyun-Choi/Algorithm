N = input()
length = 0
for i in range(1,len(N)):
    length += 9 * 10**(i-1) * i
length += (int(N) - 10**(len(N)-1) + 1) * len(N)
print(length) 

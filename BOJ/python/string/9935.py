# 1  544ms
word = input()
explosion = list(input())
stack = []
for i in word:
    stack.append(i)
    if stack[-len(explosion):] == explosion:
        del stack[-len(explosion):]
if stack: 
    print(*stack, sep='')
else: 
    print("FRULA")

# 2  248ms
target = input()
bomb = list(input())
length = len(bomb)
stack = []
last_bomb = bomb[-1]
for i in target:
    stack.append(i)
    if i == last_bomb and stack[-length:] == bomb:
        del stack[-length:]
print("FRULA" if not stack else ''.join(stack))

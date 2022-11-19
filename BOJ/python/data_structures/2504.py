bracket = input()
stack = []
tmp = 1
sum = 0
for i in range(len(bracket)):  
    if bracket[i]  == '(':
        tmp *= 2
        stack.append(bracket[i] )
    elif bracket[i]  == '[':
        tmp *= 3
        stack.append(bracket[i] )
    elif bracket[i]  == ')':
        if not stack or stack[-1] == '[':
            sum = 0
            break
        if bracket[i-1] == '(':
            sum += tmp
        tmp //= 2
        stack.pop()  
    else:
        if not stack or stack[-1] == '(':
            sum = 0
            break
        if bracket[i-1] == '[':
            sum += tmp
        tmp //= 3
        stack.pop() 
if stack:
    sum = 0
print(sum)

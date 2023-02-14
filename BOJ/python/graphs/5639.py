import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
traversal = []
while True:
    try:
        traversal.append(int(input()))
    except:
        break

def postorder(start, end):
    if start > end:
        return
    mid = end+1 
    for i in range(start+1, end+1):
        if traversal[start] < traversal[i]:
            mid = i
            break
    postorder(start+1, mid-1)
    postorder(mid, end)
    print(traversal[start])
postorder(0, len(traversal)-1)

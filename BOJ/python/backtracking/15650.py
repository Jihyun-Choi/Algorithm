def dfs(x):  
    if len(graph)==M:  
        print(*graph)  
        return

    for i in range(x+1, N+1):
        graph.append(i) 
        dfs(i)
        graph.pop() 

N, M = map(int, input().split())
graph = []
arr = [i for i in range(1, N+1)]
dfs(0)

""" 15650
DFS로 주어진 수를 graph의 배열에 넣은 후 재귀를 통해 탐색 후 빼는 방식으로 출력한다. 
오름차순으로 정렬해야된다는 조건이 있으므로 순서대로 탐색을 진행해도 중복이 일어나지 않는다.
추후에 itertools를 사용한 방법이나, 시간을 더 단축시킬 수 있는 방법에 대해 생각 후 구현해볼 예정이다.
"""

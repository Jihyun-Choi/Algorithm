K = int(input())
for i in range(K):
    N = list(map(int, input().split()))
    del N[0]
    N.sort()
    diff = [N[j+1] - N[j] for j in range(len(N)-1)]
    print('Class', i+1)
    print(f"Max {str(max(N))}, Min {str(min(N))}, Largest gap {max(diff)}")

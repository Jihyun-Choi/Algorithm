import sys
from collections import Counter
input = sys.stdin.readline
N, M = map(int, input().split())
DNA = [input().strip() for _ in range(N)]
answer = []
cnt = 0
for i, dna in enumerate(zip(*DNA)):
    counts = Counter(list(dna))
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    answer.append(sorted_counts[0][0])
    cnt += sum([cnt for key, cnt in sorted_counts[1:]])
print(''.join(answer))
print(cnt)

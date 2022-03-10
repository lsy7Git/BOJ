import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(0,N):
    x = int(input())

    if x != 0:
        heapq.heappush(heap, (abs(x), x))       # 절댓값을 우선순위로
    
    else:
        if len(heap) >= 1:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
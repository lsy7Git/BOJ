import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

for i in range(0,N):
    x = int(input())

    if x != 0:
        heapq.heappush(heap, (-x, x))     # (우선 순위, 값)
                                          # 힙에 튜플을 원소로 추가하거나 삭제하면
                                          # 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성
                                          # ex) input으로 3, 1, 5
                                          # heap = [(-3,3)]
                                          # heap = [(-3,3), (-1,1)]
                                          # heap = [(-5,5), (-1,1), (-3,3)]
    
    else:
        if len(heap) >= 1:
            print(heapq.heappop(heap)[1]) # heapq.heappop(heap)은 튜플을 반환, 두번째 요소를 반환(우선순위에는 관심이 없으므로)
        else:
            print(0)
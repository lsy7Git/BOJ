# 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, 
# N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.(deque)
# 우선, 제일 위에 있는 카드를 바닥에 버린다.(popleft)
# 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.(popleft > append)

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

Deque = deque()

for i in range(1,N+1): # 카드 순서대로 놓기
    Deque.append(i)

while len(Deque) != 1: # 마지막 한장이 남을때 까지 실행
    Deque.popleft()
    temp = Deque.popleft()
    Deque.append(temp)

print(Deque[0]) # 마지막 남은 카드를 출력
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

queue = deque()

for _ in range(0,N):
    word = input().split()
    order = word[0]

    if order == 'push':
        queue.append(int(word[1]))

    elif order == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    
    elif order == 'size':
        print(len(queue))

    elif order == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif order == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif order == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])


'''
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()

for i in range(n):
    op = input().split()
    
    if op[0] == "push":
        q.appendleft(int(op[1]))
    
    elif op[0] == "front":
        if q:
            print(q[-1])
        else:
            print(-1)
    
    elif op[0] == "back":
        if q:
            print(q[0])
        else:
            print(-1)
    
    elif op[0] == "size":
        print(len(q))
    
    elif op[0] == "empty":
        if not q:
            print(1)
        else:
            print(0)
    
    else:
        if not q:
            print(-1)
        else:
            print(q.pop())
'''
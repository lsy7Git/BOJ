# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

Deque = deque()

for _ in range(0,N):
    order = input().split()

    if order[0] == 'push_front':
        Deque.appendleft(int(order[1]))

    elif order[0] == 'push_back':
        Deque.append(int(order[1]))

    elif order[0] == 'pop_front':
        if len(Deque) != 0:
            print(Deque.popleft())
        else:
            print(-1)

    elif order[0] == 'pop_back':
        if len(Deque) != 0:
                print(Deque.pop())
        else:
            print(-1)

    elif order[0] == 'size':
        print(len(Deque))

    elif order[0] == 'empty':
        if len(Deque) == 0:
            print(1)
        else:
            print(0)
    
    elif order[0] == 'front':
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[0])

    elif order[0] == 'back':
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[-1])

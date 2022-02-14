import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    M = int(input())
    left_box = deque(map(int, input().split()))
    right_box = deque(map(int, input().split()))

    car_count = 0
    count = 0
    while left_box:
        temp = left_box.popleft()
        if temp + 1000 in right_box:
            count += 1
        if count == 2:
            count = 0
            car_count += 1

    print(car_count)


'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
car_cnt = []

for testcase in range(0,n):
    m = int(input())
    box_l = list(map(int,input().split()))
    box_r = list(map(int,input().split()))
    cnt1 = 0

    if m == 0 or m==1:
        car_cnt.append(0)
        continue

    for _ in range(0,m-1):
        cnt2 = 0

        for j in range(1,m):
            t = box_l[j] - box_l[i]

            for k in range(0,m):
                if box_r[k] <= box_l[j]:
                    continue
                if box_l[j] + t == box_r[k] or box_l[j] + t*2 == box_r[k]:
                    cnt2 += 1

        if cnt2 == 2:
            cnt1 += 1

    car_cnt.append(cnt1)

s = ''
for i in car_cnt:
    s += (str(i) + '\n')
print(s)
'''
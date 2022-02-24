# 1부터 n까지의 수를 스택에 넣었다가(push, 반드시 오름차순)
# 뽑아 늘어놓음으로써(pop) 수열 완성
# pop한 수를 나열했을 때, 입력한 수열을 만들 수 있어야 한다
# stack의 TOP(맨 위)값이 입력값보다 크면 수열을 만들 수 없다
# ex) 입력: 1, 2, 5, 3, 4
# [1] -> [] (push:1 -> pop:1) [1]
# [2] -> [] (push:2 -> pop:2) [1,2]
# [3,4,5] -> [3,4] (push:3,4,5 -> pop:5) [1,2,5]
# [3,4] -> [3] (pop:4) [1,2,5,4](입력과 다름, 따라서 NO)

import sys
input = sys.stdin.readline

n = int(input())

stack =[]
result = []
cur = 1
flag = True

for _ in range(0,n):
    num = int(input())

    while cur <= num:       # 입력한 수를 만날 때 까지 오름차순으로 push
        stack.append(cur)
        result.append('+')
        cur += 1
    
    if stack[-1] == num:    # stack의 TOP이 입력한 숫자와 같다면 pop으로 수열에 숫자 추가
        stack.pop()
        result.append('-')
    
    elif stack[-1] >= num:  # stack의 TOP이 입력값보다 크면 수열을 만들 수 없다
        print('NO')
        flag = False
        break

answer = ""

if flag:
    for i in result:
        answer += str(i) + '\n'
    print(answer)
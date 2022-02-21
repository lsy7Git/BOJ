import sys
input = sys.stdin.readline

T = int(input())

# '('이면 스택을 하나 쌓는다.
# ')'이면 바로 전 스택이 '('이고 스택 길이가 0이 아닌경우 스택에서 마지막 '('를 제거한다.
# 위 경우가 아니라면 스택에 ')'를 추가한다.
# 스택의 길이가 0이면 VPS이고 0보다 길다면 VPS가 아니다.

for _ in range(0,T):
    data = input()
    stack =[]

    for i in data:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
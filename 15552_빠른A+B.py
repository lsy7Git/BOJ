import sys
input = sys.stdin.readline # 문자열을 입력받을 때는 
                           # sys.stdin.readline().rstrip
                           # sys.stdin.readline().strip
t = int(input())

for i in range(0,t):
    a, b = map(int, input().split())
    print(a+b)

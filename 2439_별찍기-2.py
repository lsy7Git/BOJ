import sys
input = sys.stdin.readline

n = int(input())

for i in range(0,n):
    print(' ' * (n-i-1) + '*' * (i+1))

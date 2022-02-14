import sys
input = sys.stdin.readline

n = int(input())

for i in range(0,n):
    print(' '*(n-i-1)  + '*'*(2*(i+1)-1))

for i in range(n-1,0,-1):
    print(' '*(n-i)  + '*'*(2*i-1))

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
p = True

for _ in range(M):
    i = int(input())
    k = list(map(int, input().split()))

    for j in range(i-1):  # 더미에 있는 책이 내림차순인지 확인(아래부터 위로)
        if k[j] < k[j+1]:
            p = False
            break

        if not p: 
            break

print('Yes' if p else 'No') # p가 True면 Yes, False면 No
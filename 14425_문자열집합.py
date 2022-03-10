import sys

input = sys.stdin.readline

N, M = map(int, input().split())

S = set()             # 빈 집합 생성
count = 0

for _ in range(0,N):  # 집합에 원소 추가(집합은 중복 허용X)
    input_S = input().rstrip()
    S.add(input_S)

for _ in range(0,M):  
    input_M = input().rstrip()

    if input_M in S:  # 집합에 항목이 있는지 확인
        count += 1

print(count)
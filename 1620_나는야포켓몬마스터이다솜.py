import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pokemon_name = {} # 포켓몬이름 : 포켓몬넘버
pokemon_num = {}  # 포켓몬넘버 : 포켓몬이름

for i in range(1, N+1):
    name = input().rstrip()
    pokemon_num[i] = name
    pokemon_name[name] = i

for _ in range(0,M):
    q = input().rstrip()

    if q.isdigit(): # 숫자인지 판별
        print(pokemon_num[int(q)])
    else:
        print(pokemon_name[q])
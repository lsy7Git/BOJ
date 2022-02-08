# 이용한 통화의 개수 N(N은 20보다 작거나 같은 자연수)
# 둘째 줄에 통화 시간 N개. 통화 시간은 10,000보다 작거나 같은 자연수

n = int(input())
fee = list(map(int, input().split()))

Y = [] # 영식 요금제: 30초마다 10원
for i in fee:
    if i < 30:
        Y.append(10)
    else:
        Y.append((i//30+1)*10)

M = [] # 민식 요금제: 60초마다 15원
for i in fee:
    if i < 60:
        M.append(15)
    else:
        M.append((i//60+1)*15)

if sum(Y) == sum(M):
    print('Y', 'M', sum(Y))
elif sum(Y) < sum(M):
    print('Y', sum(Y))
elif sum(M) < sum(Y):
    print('M', sum(M))

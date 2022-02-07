cnt = [0, 0, 0] # 배(0)의 개수
result = []
for i in range(0,3):
    yut = list(map(int, input().split()))
    

    for j in range(0,4):
        if yut[j] == 0:
            cnt[i] += 1

    if cnt[i] == 1:
        result.append('A')
    elif cnt[i] == 2:
        result.append('B')
    elif cnt[i] == 3:
        result.append('C')
    elif cnt[i] == 4:
        result.append('D')
    else:
        result.append('E')

for i in range(0,3):
    print(result[i])

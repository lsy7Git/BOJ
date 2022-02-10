# 1부터 20까지 숫자가 하나씩 쓰인 20장의 카드
card = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# 총 10개의 줄에 걸쳐 한 줄에 하나씩 10개의 구간
# i번째 구간의 시작 위치 ai와 끝 위치 bi가 차례대로 주어진다.(1 ≤ ai ≤ bi ≤ 20)
for i in range(0,10):
    a, b = map(int, input().split())
    
    if a == 1:
        card[0:b] = card[b-1::-1]
    elif a != b:
        card[a-1:b] = card[b-1:a-2:-1]

for i in card:
    print(i, end=' ')

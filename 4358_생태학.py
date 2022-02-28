import sys
input = sys.stdin # 여러줄을 입력 받을 때
                  # sys.stdin은 ^Z를 입력받으면 종료, 개행문자까지 입력

Trees = {}
tree_cnt = 0

for line in input:
    if line == '\n':        # 개행문자만 입력됐을 경우 종료
        break

    tree = line.rstrip()
    tree_cnt += 1

    if tree in Trees:   
        Trees[tree] += 1    # 딕셔너리에 이미 있는 key면 value +1
    else:
        Trees[tree] = 1     # 딕셔너리에 없는 key면 key와 value=1 추가

Trees = sorted(Trees.items(), key = lambda x : x[0]) # key 값을 기준으로 정렬

def tree_percent(a):
    percent = round((a / tree_cnt) * 100, 4) #소수점 5번째 자리에서 반올림
    return percent

for k, v in Trees:
    percent = tree_percent(v)
    print(k, '%.4f' %percent) # 소수점 4자리까지 출력
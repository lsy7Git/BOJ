import sys
input = sys.stdin.readline

T = int(input())

for i in range(0, T):
    N = int(input())
    test_case = sorted(map(int, input().split()), reverse=True) # 입력 받은 가격을 내림차순으로 정렬
    P = []
    
    while test_case: # test_case의 원소가 빌 때까지 while문을 통해 반복 수행
        
        temp = test_case.pop() # 제일 작은 값부터 호출
                               # pop() 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제

        if int(temp * 100/75) in test_case: # 호출한 값에 원가가 test_case에 있는지 확인(temp * 100/75)
            P.append(str(temp))
            test_case.remove(int(temp * 100/75)) # 중복해서 찾는것을 방지하기 위해 원가를 test_case에서 삭제

    print("Case #%d: %s" % (i+1, ' '.join(P)))

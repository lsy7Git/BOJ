num1, num2 = map(int, input().split())

if num1 == num2:
    print(0)
    print()

elif num1 < num2:
    cnt = num2 - num1 - 1
    print(cnt)
    for i in range(num1+1, num2):
        print(i, end=' ')

elif num2 < num1:
    cnt = num1 - num2 - 1
    print(cnt)
    for i in range(num2+1, num1):
        print(i, end=' ')

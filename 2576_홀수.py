numbers = []

for i in range(0,7):
    n = int(input())
    numbers.append(n)

odd_sum = 0
odd_min = 100

for i in numbers:
    if i%2 == 1:
        odd_sum += i

        if i < odd_min:
            odd_min = i

if odd_sum == 0:
    print(-1)
else:
    print(odd_sum)
    print(odd_min)

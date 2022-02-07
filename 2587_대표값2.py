numbers = []

for i in range(0,5):
    n = int(input())
    numbers.append(n)

numbers = sorted(numbers)

num_sum = 0

for i in numbers:
    num_sum += i

num_avg = int(num_sum / 5)
num_median = numbers[2]

print(num_avg)
print(num_median)

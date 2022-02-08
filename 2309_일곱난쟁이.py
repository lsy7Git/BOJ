height = []
for i in range(0,9):
    height.append(int(input()))

height_ex = sum(height) - 100

for i in range(0,8):
    for j in range(i+1,9):
        if height[i] + height[j] == height_ex:
            r1 = height[i]
            r2 = height[j]

height.remove(r1)
height.remove(r2)

height = sorted(height)
for i in height:
    print(i)

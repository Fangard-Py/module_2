import random

first_stone = random.choice(range(3, 20))
print(first_stone)

result = ''
for i in range(1, 21):
    for j in range(1 + i, 21):
        if i + j > first_stone:
            break
        elif first_stone % (i + j) == 0:
            result += str(i) + str(j)
            print(result)

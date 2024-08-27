import random
result = str()
first_stone = []
second_stone = range(1, 20)
rand_num = random.choice(range(3, 20))
first_stone.append(rand_num)
print(first_stone)
for i in first_stone:
    for j in second_stone:
        if i % j == 0:
            result += f'{j}'
            print(f'{first_stone} - {result}')

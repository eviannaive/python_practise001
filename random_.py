import random

print(dir(random))

# randint
print(random.randint(1, 10))

# random 0~1之間的浮點數
print(random.random())

options = ['f','w','g','s','3','c']
rand_option = random.choice(options)
print(rand_option)

#打亂列表
random.shuffle(options)
print(options)
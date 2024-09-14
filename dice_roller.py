import random

list=[]

try:
    quantity = int(input("請輸入骰子數量："))
    for i in range(quantity):
        list.append(random.randint(1,6))
    print(list,sum(list))
except ValueError:
    print("請輸入整數")



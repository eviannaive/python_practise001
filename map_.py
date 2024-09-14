# map(函式,可迭代的列表)

store = [
    ("上衣",300),
    ("褲子",200),
    ("洋裝",1200),
    ("皮帶",100),
]

loop_item = lambda i : (f"品項：{i[0]}",f"價錢：{i[1]}")

items = list(map(loop_item, store))
print(items)

filter_price = lambda i : i[1] >= 300

filter_result = list(filter(filter_price, store))
print(filter_result)

def square(x):
    return x ** 2
numbers = []
for i in range(1,11):
    numbers.append(square(i))
print(numbers)

square2 = [ i ** 2 for i in range(1,11) ]
print(square2)

grades = [60,30,70,94,87]
new_grades = [f"{(i*1.1):.2f}" for i in grades if i >=70]
print(f"篩選後並更新的分數為：{new_grades}")
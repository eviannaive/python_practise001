menu = {
    "pizza": 300,
    "popcorn": 200,
    "fries": 120,
    "bread": 80,
    "water": 50
}

cart = [

]
total = 0
print("菜單：")
print("---------------")

for item, price in menu.items():
    print(f"{item}: {price}")

while True:
    food = input("請輸入一個項目(輸入q結束):")
    if food.lower() == "q":
        break
    elif menu.get(food) is None:
        print("沒有這個商品")
    else:
        cart.append(food)
        total += menu.get(food)
for item in cart:
    print(item, end=",")
print()
print(f"總金額為 ${total:,.2f}")

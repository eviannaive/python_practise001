# list, set, tuple

goods = []
prices = []

# 無窮迴圈
while True:
    good = input("請輸入想購買的物品：")
    if good.lower() == "q":
        break

    price = float(input(f"請輸入 {good} 的價格："))
    goods.append(good)
    prices.append(price)

print("商品列表：", goods)
print("價格清單：", prices)

for index, good in enumerate(goods):
    # print("index:", index)
    # print("商品名稱:", good)
    print(f"第{index+1}個商品是{good},價格是{prices[index]:.2f}")

total = sum(prices)
print(f"總價是${total:,.2f}")

# 這樣會報錯，一定要用enumerate
# for index, good in goods:
#     print("index:", index)
#     print("商品名稱:", good)

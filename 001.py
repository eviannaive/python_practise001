rows = int(input("請輸入行數："))
cols = int(input("請輸入列數："))
symbol = str(input("請輸入符號："))

for i in range(rows):
    for j in range(cols):
        print(symbol,end="")
    print("")
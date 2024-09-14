import random

def main():
    count = 0
    print("歡迎來到猜數字遊戲！")
    while True:
        try:
            max=int(input("請設定最大數字："))
            break
        except ValueError:
            print("數字須為整數")

    while True:
        try:
            min=int(input("請設定最小數字："))
            if min>=max:
                print(f"數字須小於{max}")
                continue
            break
        except ValueError:
            print("數字須為整數")

    print(f"初始化遊戲中{'.'*16}")
    num = random.randint(min,max)
    while True:
        try:
            guess = int(input(f"猜一個 {min} ~ {max} 之間的數字："))
            if(guess == num):
                print(f"恭喜您猜對了！數字是 {num}，總共猜了 {count} 次！")
                count+=1
                break
            elif guess > max or guess < min:
                print(f"數字須介於 {min} ~ {max} 之間")
            elif(guess > num):
                max = guess
                count += 1
            elif(num > guess):
                min = guess
                count += 1
        except ValueError:
            print("輸入值須為數字")

main()

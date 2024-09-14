import random

options = ['rock','paper','scissors']

def main():

    while True:
        print("請輸入 (",end="")
        print("/".join(options), end=")，結束請輸入(q):")
        # for item in options:
        #     print(f"{item}", end="/")
        you = input("").strip().lower()
        if you == 'q':
            print("已退出遊戲")
            break
        if you not in options:
            print("無效的內容")
            continue

        you_index = options.index(you)
        computer = random.randint(0, 2)

        if(options[you_index - 1] == options[computer]):
            print(f'對手出{options[computer]}，you win!')
        elif(you_index == computer):
            print(f"對手出{options[computer]}，平手")
        else:
            print(f'對手出{options[computer]}，you lose')

main()
# args => arguments 任意數量的參數 * => tuple


def add(*args):
    total = 0
    for arg in args:
        print(f"arg: {arg}")
        total += arg
    return total

print(add(5,3,6,4,0,4))


# kwargs => 關鍵字 + args ，用字典儲存元素
# 傳數任意參數

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"key:{key} ,value:{value}")

print_info(name="lalala",gg="dsjaldakd",mmm="fsdfsf")
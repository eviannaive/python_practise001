def double(x):
    return x * 2

double2 = lambda x : x *2

print(double2(5))

def summary(a,b):
    return a*b

summary2 = lambda x,y:x*y
print(summary(3,5))

def result(x):
    if x % 2 == 0:
        print(f"{x}是偶數")
    else:
        print(f"{x}是奇數")

result2 = lambda x : f"{x}是偶數" if x % 2 == 0 else f"{x}是奇數"

print(result2(10))
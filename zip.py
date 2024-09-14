users = ["amy","jack","cindy"]
ages= [30,22,56]
job =["designer","engineer"]

result = zip(users,ages) #這只能loop一次?!
# result = list(zip(users,ages)) #這樣才能一直使用
result2 = zip(users, ages, job)
print(list(result2)) # job數組少一個，所以只會串兩個


# for i in result:
#     print(i)
#
# print(list(map(lambda x:f"{x[0]}的年齡是{x[1]}",list(result))))


result_dict = dict(result)
for k,v in result_dict.items():
    print(f"{k},{v}")


# 元組：[(value[0],value[1],value[2]),(value[0],value[1],value[2]), ...] 要用 list(元組) 才能loop
# 字典：{key: value, key: value, ...} 要用 (字典).items() 才能loop
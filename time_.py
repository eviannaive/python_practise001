import time

print(time.ctime(0))
print(time.time())
print(time.localtime()) #時間物件
print("格式化時間",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

# 轉成時間物件
time_str = "2024-10-8 16:27:8"
time_obj = time.strptime(time_str,"%Y-%m-%d %H:%M:%S")
print(time_obj)
print(time_obj.tm_hour)
print(time_obj.tm_min)
print(time_obj.tm_sec)
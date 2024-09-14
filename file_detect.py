import os

file = r"/Users/evianna/Desktop/work"

if os.path.exists(file):
    print("資料夾存在")
else:
    print("資料夾不存在")
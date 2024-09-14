
data = {
    "a": 1,
    "b": 30,
    "c": 33,
    "d": 80
}

data2 = { key: f"{(value * 0.89):.2f}" for key,value in data.items() if value > 30}
print(data2)
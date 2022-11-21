

def func():
    idx = 5
    while idx <= 5:
        for i in range(10):
            idx = i
            return True, i


x = func()

print(x[1])


def fibonacci(x):
    if x == 1:
        return 1
    return x * fibonacci(x-1)

x = 6
print(fibonacci(x))

# def fibonacci(x):
#     if x == 1:
#         return 1
#     return x * fibonacci(x-1)

# x = 6
# print(fibonacci(x))


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage
n_terms = 10
for i in range(n_terms):
    print(fibonacci(i))

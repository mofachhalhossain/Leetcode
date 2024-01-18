# Dynamic Solution
def fibonacci(n):
    a = [1]
    if n == 1:
        return a
    a.append(1)
    for i in range(1, n):
     a.append(a[i]+a[i-1])
    return a[len(a)-1]


n = 4
print(fibonacci(n))
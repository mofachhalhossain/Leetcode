def trailingZeroes(n):
    c = 0
    while n > 0:
        n //= 5
        c += n
    return c



n = 5
u = trailingZeroes(n)
print(u)
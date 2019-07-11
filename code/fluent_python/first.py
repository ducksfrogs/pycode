def factorial(n):
    return 1 if n < 2 else n* factorial(n-1)


a = factorial(2)

b = factorial(10)
print(a)
print(b)

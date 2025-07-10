def factorial(n):
    f = n
    if n == 0:
        return 1
    f = f*factorial(n-1)
    return f


fact = factorial(5)
print(fact)

# 5!= 5*4*3*2*1

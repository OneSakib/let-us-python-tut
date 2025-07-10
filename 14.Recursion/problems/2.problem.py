def factorize(n, i):
    if i <= n:
        if n % i == 0:
            n = n//i
            print("Fac: {}: {}".format(i, n))
        else:
            i += 1
        factorize(n, i)


num = int(input("Enter a num:"))
print("Prime Factor are: ")
factorize(num, 2)


# 50 factor 2,5,5

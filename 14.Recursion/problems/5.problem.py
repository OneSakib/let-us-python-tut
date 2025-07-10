# fibbonacci series
# sum of two previos value
# 1  1 2 3 5 8


# def fibbo(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibbo(n-1) + fibbo(n-2)

# print(fibbo(10))


def fibbo(old, current, terms):
    if terms >= 1:
        new = old+current
        print(f"{new}", end="\t")
        terms -= 1
        fibbo(current, new, terms)


old = 1
current = 1
print(f"{old}", end="\t")
print(f"{current}", end="\t")
fibbo(old, current, 13)

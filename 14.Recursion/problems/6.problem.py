import sys


def dec_to_binary(n):
    r = n % 2
    n = int(n/2)
    if n != 0:
        dec_to_binary(n)
    print(r, end="")


num = 32
print(f"Binary :",end="\t")
dec_to_binary(num)

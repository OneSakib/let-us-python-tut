# sum of digits 345=3+4+5

# def rsum(num):
#     total = 0
#     if num != 0:
#         total += num % 10
#         total+=rsum(num//10)
#     return total


# total = rsum(222)
# print(total)
def rsum(num):    
    if num != 0:
        digit = num % 10
        num = int(num/10)
        sum = digit + rsum(num)
    else:
        return 0
    return sum


total = rsum(222)
print(total)

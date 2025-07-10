def sum_of_natural(no):
    total = 0
    if no == 0:
        return 0
    else:
        total += no+sum_of_natural(no-1)
        return total


num = 25
print(f"Sum of First {num} Natural Number is : {sum_of_natural(num)}")

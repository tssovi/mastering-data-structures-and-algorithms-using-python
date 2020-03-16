def factorial(n):
    if n == 1:
        return 1
    else:
        return (n * factorial(n - 1))


def print_number_rev(n):
    if n > 0:
        print(n)
        print_number_rev(n - 1)


def print_number(n):
    if n > 0:
        print_number(n - 1)
        print(n)


num = 5

print_number_rev(num)
print_number(num)
print("The factorial of", num, "is", factorial(num))

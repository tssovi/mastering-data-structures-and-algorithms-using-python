# normal recursive of factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# tail recursive version of factorial
def tail_factorial(n, num=1):
    if n == 0:
        return num
    else:
        return tail_factorial(n - 1, num * n)

# head recursive version of factorial
def head_factorial(n, num=1):
    if n > 0:
        return head_factorial(n - 1, num * n)
    else:
        return num

# for loop version of factorial
def loop_factorial(n):
    num = 1
    for i in range(1, n + 1):
        num = num * i
    return num



print(factorial(5))
print(tail_factorial(5))
print(head_factorial(5))
print(loop_factorial(5))
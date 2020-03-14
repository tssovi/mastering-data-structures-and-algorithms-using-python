# Math related common functions

# Random integer number
integer = -10
print('Absolute value of -10 is:', abs(integer))

# Random floating number
floating = -10.33
print('Absolute value of -10.33 is:', abs(floating))

# Random complex number
complex = (5 - 2j)
print('Magnitude of 5 - 2j is:', abs(complex))

# divmod() with intiger numbers
print('Divmod of 7 and 2 is:', divmod(7, 2))

# divmod() with Floats
print('Divmod of 7.5 and 2.5 is:', divmod(7.5, 2.5))

# Enumerate example
grocery = ['bread', 'milk', 'butter']

for count, item in enumerate(grocery):
    print(count, item)

# changing default start value
for count, item in enumerate(grocery, 100):
    print(count, item)

# Max value from a list
numbers = [3, 2, 8, 5, 10, 6]
largest_number = max(numbers)

print("The largest number from numbers list is:", largest_number)

# Max value from a list
numbers = [3, 2, 8, 5, 10, 6]
smallest_number = min(numbers)

print("The smallest number from numbers list is:", smallest_number)

# Power calculation
x = 7
y = 2
z = 5

print('Power of x & y is:', pow(x, y))
print('Power of x, y & z is:', pow(x, y, z))

# Round numbers
x = 5.756

print('Round of x without decimal points is:', round(x))
print('Round of x for 2 decimal points is:', round(x, 2))

# Sum of a list
numbers = [2.5, 3, 4, -5]

# start parameter is not provided
numbers_sum = sum(numbers)
print('Sum of all variable in numbers list is:', numbers_sum)

# start = 10
numbers_sum = sum(numbers, 10)
print('Sum of all variable in numbers list with 10 is:', numbers_sum)

# Slice to get a substring from the given string
string = 'Python'

# stop = 3
# contains 0, 1 and 2 indices
slice_object = slice(3)
print('Substing of Python is:', string[slice_object])

# start = 1, stop = 6, step = 2
# contains 1, 3 and 5 indices
slice_object = slice(1, 6, 2)
print('Substing of Python is:', string[slice_object])
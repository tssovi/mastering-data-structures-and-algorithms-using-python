# Here a is int
a = 5
print(a, "is of type", type(a))

# Here a is float
a = 2.0
print(a, "is of type", type(a))

# Here a is complex
a = 1+2j
print(a, "is of type", type(a))

# Here a is list
a = [1, 2.2, 'python']
print(a, "is of type", type(a))

# List is mutable
a = [1, 2.2, 'python']
a[2] = 'list is mutable'
print(a)

# Here a is tuple
a = (1, 2.2, 'python')
print(a, "is of type", type(a))

# Tuple is immutable
a = (1, 2.2, 'python')
try:
    a[2] = 'tuple is immutable'
except:
    print('Tuple is immutable')
print(a)

# Here a is single string
a = "This is a string"
print(a, "is of type", type(a))

# Here a is multiline string
a = '''This is a multiline string
Line 1
Line 2'''
print(a, "is of type", type(a))

# Here a is set
a = {1,2,2,3,3,3}
print(a, "is of type", type(a))

# Here a is dict
a = {'key1':'value1','key2':'value2'}
print(a, "is of type", type(a))

person = {"name": "John", "age": 23, "sex": "male"}

# Here a is frozenset of person dict
a = frozenset(person)
print(a, "is of type", type(a))

# Here a is boolean
a = True
print(a, "is of type", type(a))


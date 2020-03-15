# Instead of adding line1, line2 to text individually, use list and join
# Don’t do this:

text = 'line1\n'
text += 'line2'
print(text)

# Better do this
list=['line1', 'line2']
text = '\n'.join(list)
print(text)

# Don’t use the + operator for concatenation if you can avoid it
# Don’t do this
msg = '+ operator'
full_msg = 'Avoid using the ' + msg + ' for strings'
print(full_msg)

# Better do this
full_msg = 'Avoid using the %s for strings' % msg
print(full_msg)

# Or this
full_msg = 'Avoid using the {} for strings'.format(msg)
print(full_msg)

# Assign a function to a local variable
class MathFunctions():
    def sum(a, b):
        return a + b

sum = MathFunctions.sum
a = 5
b = 6

res = sum(a, b)
print('Summation of a and b is:', res)

# Use builtin functions and libraries rather than raw codes
# Don’t do this
word_list = ['python', 'is', 'awesome']
new_list = []
for myword in word_list:
      new_list.append(myword.upper())
print(new_list)

# Better do this
new_list = map(str.upper, word_list)

# Convert map object to tuple to print
print(tuple(new_list))

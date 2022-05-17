"""
Identity operators:

    is and is not are the identity operators in Python. They are used to check if two values (or variables) are located on the same part of the memory. Two variables that are equal does not imply that they are identical.

    Operator	Meaning	Example
    is	True if the operands are identical (refer to the same object)	x is True
    is not	True if the operands are not identical (do not refer to the same object)	x is not True

Membership Operator:

    in True if the operands are identical (refer to the same object)	x is True
    not in True if the operands are not identical (do not refer to the same object)	x is not True

"""


# Identity Operator:

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)


# Membership Operator:

x = 'Hello world'
y = {1: 'a', 2: 'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)
